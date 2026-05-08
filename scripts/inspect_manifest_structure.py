#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Inspect MANIFEST document structure for tabs and nested content.
Helps understand the actual Google Docs API structure before implementing improvements.
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

def inspect_manifest():
    """Inspect MANIFEST structure and output findings."""
    credentials = get_credentials()
    service = build('docs', 'v1', credentials=credentials)

    # Get document with tab content
    doc = service.documents().get(
        documentId=MANIFEST_DOC_ID,
        includeTabsContent=True
    ).execute()

    print("=" * 80)
    print("📄 MANIFEST STRUCTURE INSPECTION")
    print("=" * 80)

    # Document metadata
    print(f"\n📋 Document Title: {doc.get('title', 'N/A')}")
    print(f"📋 Document ID: {MANIFEST_DOC_ID}")

    # Check for body content
    body = doc.get('body', {})
    body_content = body.get('content', [])
    print(f"\n🔍 body.content exists: {len(body_content) > 0}")
    print(f"   Elements in body.content: {len(body_content)}")

    # Check for tabs
    tabs = doc.get('tabs', [])
    print(f"\n📑 Tabs structure:")
    print(f"   Total tabs found: {len(tabs)}")

    if tabs:
        for idx, tab in enumerate(tabs):
            tab_id = tab.get('tabId', 'N/A')
            tab_title = tab.get('title', 'N/A')
            document_tab = tab.get('documentTab', {})
            tab_body = document_tab.get('body', {})
            tab_content = tab_body.get('content', [])

            print(f"\n   Tab {idx}:")
            print(f"      tabId: {tab_id}")
            print(f"      title: {tab_title}")
            print(f"      body.content elements: {len(tab_content)}")

            # Check for nested tabs (childTabs)
            child_tabs = tab.get('childTabs', [])
            if child_tabs:
                print(f"      ⚠️  childTabs (nested): {len(child_tabs)}")
                for child_idx, child_tab in enumerate(child_tabs):
                    child_id = child_tab.get('tabId', 'N/A')
                    child_title = child_tab.get('title', 'N/A')
                    print(f"         Child Tab {child_idx}: {child_id} ({child_title})")
    else:
        print("   ❌ No tabs found (non-tabbed document)")

    # Search for "Issue #21" in all content
    print(f"\n🔎 Searching for 'Issue #21' in document:")

    found_locations = []

    # Search in body.content
    if body_content:
        for elem_idx, elem in enumerate(body_content):
            if 'paragraph' in elem:
                para = elem['paragraph']
                for run_idx, run in enumerate(para.get('elements', [])):
                    if 'textRun' in run:
                        text = run['textRun'].get('text', '')
                        if 'Issue #21' in text:
                            found_locations.append({
                                'location': 'body.content',
                                'element': f'paragraph[{elem_idx}]',
                                'run': run_idx,
                                'text_snippet': text[:50]
                            })

    # Search in tabs
    for tab_idx, tab in enumerate(tabs):
        doc_tab = tab.get('documentTab', {})
        tab_body = doc_tab.get('body', {})
        tab_content = tab_body.get('content', [])
        tab_id = tab.get('tabId', 'N/A')

        for elem_idx, elem in enumerate(tab_content):
            if 'paragraph' in elem:
                para = elem['paragraph']
                for run_idx, run in enumerate(para.get('elements', [])):
                    if 'textRun' in run:
                        text = run['textRun'].get('text', '')
                        if 'Issue #21' in text:
                            found_locations.append({
                                'location': f'tabs[{tab_idx}].documentTab.body.content',
                                'tabId': tab_id,
                                'element': f'paragraph[{elem_idx}]',
                                'run': run_idx,
                                'text_snippet': text[:50]
                            })

    if found_locations:
        print(f"\n   ✅ Found {len(found_locations)} location(s):")
        for loc in found_locations:
            print(f"\n      Location: {loc['location']}")
            print(f"      Element: {loc['element']}")
            if 'tabId' in loc:
                print(f"      tabId: {loc['tabId']}")
            print(f"      Text: {loc['text_snippet']}...")
    else:
        print(f"\n   ❌ 'Issue #21' NOT found in document")

    # Summary and recommendations
    print(f"\n" + "=" * 80)
    print("📊 SUMMARY & RECOMMENDATIONS")
    print("=" * 80)

    if tabs:
        print(f"\n✅ Document has tab structure (tabbed mode)")
        nested = any(t.get('childTabs') for t in tabs)
        if nested:
            print(f"⚠️  Document has NESTED tabs (childTabs)")
            print(f"   → Need RECURSIVE tab traversal")
        else:
            print(f"   Document has FLAT tab structure")
            print(f"   → Can use simple iteration")

        if found_locations:
            location = found_locations[0]
            if 'tabId' in location:
                print(f"\n📍 Issue #21 found in: {location['tabId']}")
            else:
                print(f"\n📍 Issue #21 found in: body.content (not in tabs)")
        else:
            print(f"\n⚠️  Issue #21 NOT found (search failure or missing section)")
    else:
        print(f"\n📄 Document is NON-TABBED (traditional single-body structure)")
        if found_locations:
            print(f"✅ Issue #21 found in: body.content")
        else:
            print(f"❌ Issue #21 NOT found")

    # JSON output for detailed inspection
    output_file = "MANIFEST_structure_inspection.json"
    inspection_data = {
        'document_id': MANIFEST_DOC_ID,
        'document_title': doc.get('title'),
        'has_body_content': len(body_content) > 0,
        'body_content_count': len(body_content),
        'has_tabs': len(tabs) > 0,
        'tabs_count': len(tabs),
        'has_nested_tabs': any(t.get('childTabs') for t in tabs),
        'issue_21_locations': found_locations
    }

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(inspection_data, f, indent=2, ensure_ascii=False)

    print(f"\n💾 Detailed JSON output saved to: {output_file}")
    print("\n" + "=" * 80)

if __name__ == '__main__':
    try:
        inspect_manifest()
    except Exception as e:
        print(f"❌ Error: {e}")
        exit(1)
