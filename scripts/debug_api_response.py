#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Debug API response structure to understand element format.
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

def debug_api_response():
    """Debug API response structure."""
    credentials = get_credentials()
    service = build('docs', 'v1', credentials=credentials)

    # Get document with tabs content
    doc = service.documents().get(
        documentId=MANIFEST_DOC_ID,
        includeTabsContent=True
    ).execute()

    tabs = doc.get('tabs', [])

    if not tabs:
        print("No tabs found")
        return

    document_tab = tabs[0].get('documentTab', {})
    body = document_tab.get('body', {})
    content = body.get('content', [])

    print("=" * 80)
    print("📊 API RESPONSE STRUCTURE ANALYSIS")
    print("=" * 80)
    print(f"\nTotal content elements: {len(content)}")

    # Examine first few paragraphs in detail
    print(f"\n📌 First 3 paragraph elements (raw JSON):")

    for elem_idx in range(min(3, len(content))):
        elem = content[elem_idx]
        print(f"\n   Element {elem_idx}:")
        print(f"      Keys: {list(elem.keys())}")

        if 'paragraph' in elem:
            para = elem['paragraph']
            print(f"      paragraph.Keys: {list(para.keys())}")

            elements = para.get('elements', [])
            print(f"      elements count: {len(elements)}")

            for run_idx in range(min(2, len(elements))):
                run = elements[run_idx]
                print(f"\n      Element {run_idx}:")
                print(f"         Keys: {list(run.keys())}")

                # Print first element in full
                if run_idx == 0:
                    print(f"         Full content: {json.dumps(run, indent=12, ensure_ascii=False)[:500]}")

    # Look for Issue #21 by searching through element type distribution
    print(f"\n\n📊 Element type distribution:")
    element_types = {}

    for elem_idx, elem in enumerate(content):
        if 'paragraph' in elem:
            para = elem['paragraph']
            for run in para.get('elements', []):
                for key in run.keys():
                    if key not in element_types:
                        element_types[key] = 0
                    element_types[key] += 1

    for elem_type, count in sorted(element_types.items(), key=lambda x: -x[1]):
        print(f"   {elem_type}: {count}")

    # Find paragraphs with any text-like content
    print(f"\n\n🔎 Searching for text content (all element types):")

    search_markers = ['Issue', 'Engagement', '#21']
    found_any = False

    for elem_idx, elem in enumerate(content):
        if 'paragraph' in elem:
            para = elem['paragraph']
            # Convert element to JSON and search
            elem_json = json.dumps(para, ensure_ascii=False)

            for marker in search_markers:
                if marker in elem_json:
                    found_any = True
                    print(f"\n   ✓ Found '{marker}' in element {elem_idx}")
                    # Extract context
                    idx = elem_json.find(marker)
                    context_start = max(0, idx - 100)
                    context_end = min(len(elem_json), idx + len(marker) + 100)
                    context = elem_json[context_start:context_end]
                    print(f"      Context: ...{context}...")
                    break

    if not found_any:
        print(f"   No markers found in any elements")

if __name__ == '__main__':
    try:
        debug_api_response()
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        exit(1)
