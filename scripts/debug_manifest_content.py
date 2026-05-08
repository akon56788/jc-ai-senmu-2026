#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Debug script to examine actual text content in MANIFEST document.
Helps identify why Issue #21 detection is failing.
"""

from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import json
from pathlib import Path
import sys

# UTF-8 encoding support for Windows
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

MANIFEST_DOC_ID = "1guHY4inY_lXrpxVkHepT9Fi0-7xjoObF4SQsNw3w1tA"
OAUTH_TOKEN_FILE = Path.home() / ".claude" / "google_oauth_token.json"
SCOPES = ['https://www.googleapis.com/auth/documents']

def get_credentials():
    """Load stored OAuth credentials."""
    if not OAUTH_TOKEN_FILE.exists():
        raise FileNotFoundError(f"OAuth token not found: {OAUTH_TOKEN_FILE}")

    creds = Credentials.from_authorized_user_file(str(OAUTH_TOKEN_FILE), SCOPES)

    if creds.expired and creds.refresh_token:
        creds.refresh(Request())
        with open(OAUTH_TOKEN_FILE, 'w') as f:
            f.write(creds.to_json())

    return creds

def debug_manifest():
    """Debug MANIFEST content extraction."""
    credentials = get_credentials()
    service = build('docs', 'v1', credentials=credentials)

    # Get document with tabs content
    doc = service.documents().get(
        documentId=MANIFEST_DOC_ID,
        includeTabsContent=True
    ).execute()

    print("=" * 80)
    print("🔍 MANIFEST CONTENT DEBUG")
    print("=" * 80)

    # Get tabs content
    tabs = doc.get('tabs', [])
    print(f"\n📑 Tabs found: {len(tabs)}")

    for tab_idx, tab in enumerate(tabs):
        print(f"\n📌 Tab {tab_idx}:")
        document_tab = tab.get('documentTab', {})
        body = document_tab.get('body', {})
        content = body.get('content', [])

        print(f"   Content elements: {len(content)}")

        # Extract all text and show first/last paragraphs
        all_text_pieces = []

        for elem_idx, elem in enumerate(content):
            if 'paragraph' in elem:
                para = elem['paragraph']
                elements = para.get('elements', [])

                # Print paragraph metadata
                paragraph_text = ''
                for run_idx, run in enumerate(elements):
                    if 'textRun' in run:
                        text = run['textRun'].get('text', '')
                        paragraph_text += text
                        all_text_pieces.append(text)

                # Show paragraphs containing potential markers
                if any(marker in paragraph_text for marker in ['Issue', 'Engagement', '#21']):
                    print(f"\n   🎯 Interesting paragraph at index {elem_idx}:")
                    print(f"      Text: {repr(paragraph_text[:100])}")
                    if len(paragraph_text) > 100:
                        print(f"      ...{repr(paragraph_text[-50:])}")

        # Print first 5 and last 5 paragraphs
        print(f"\n   📄 First 3 paragraphs:")
        for elem_idx in range(min(3, len(content))):
            elem = content[elem_idx]
            if 'paragraph' in elem:
                para = elem['paragraph']
                text = ''.join([
                    run.get('text', '')
                    for run in para.get('elements', [])
                    if 'textRun' in run
                ])
                print(f"      [{elem_idx}]: {repr(text[:80])}")

        print(f"\n   📄 Last 3 paragraphs:")
        for elem_idx in range(max(0, len(content) - 3), len(content)):
            elem = content[elem_idx]
            if 'paragraph' in elem:
                para = elem['paragraph']
                text = ''.join([
                    run.get('text', '')
                    for run in para.get('elements', [])
                    if 'textRun' in run
                ])
                print(f"      [{elem_idx}]: {repr(text[:80])}")

        # Full text search for Issue #21
        full_text = ''.join(all_text_pieces)
        print(f"\n   🔎 Searching in {len(all_text_pieces)} text pieces:")
        print(f"      Total text length: {len(full_text)} characters")

        markers = ['Issue #21', 'Issue', '#21', 'Engagement System', '## 🎯']
        for marker in markers:
            if marker in full_text:
                idx = full_text.find(marker)
                context_start = max(0, idx - 50)
                context_end = min(len(full_text), idx + len(marker) + 50)
                context = full_text[context_start:context_end]
                print(f"      ✓ Found '{marker}':")
                print(f"        ...{repr(context)}...")
            else:
                print(f"      ✗ NOT found: '{marker}'")

if __name__ == '__main__':
    try:
        debug_manifest()
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        exit(1)
