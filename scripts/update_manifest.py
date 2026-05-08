#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Update Google Docs MANIFEST with Issue #21 Engagement System Files section.

Uses OAuth 2.0 for authentication with Google Docs API.
Credentials file: ~/.claude/credentials.json

Usage:
    python scripts/update_manifest.py
"""

from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import os
import sys
import json
import argparse
from pathlib import Path

# Set UTF-8 output for Windows compatibility
if sys.stdout.encoding != 'utf-8':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# MANIFEST document ID (正本 Drive SSOT - Issue #19 確認済み)
MANIFEST_DOC_ID = "1guHY4inY_lXrpxVkHepT9Fi0-7xjoObF4SQsNw3w1tA"

# Google OAuth credentials file location
CREDENTIALS_FILE = Path.home() / ".claude" / "credentials.json"
OAUTH_TOKEN_FILE = Path.home() / ".claude" / "google_oauth_token.json"

# Scopes required for Google Docs API
SCOPES = ['https://www.googleapis.com/auth/documents']

# Content to add
ENGAGEMENT_SYSTEM_SECTION = """

## 🎯 Issue #21: Engagement System Files (エンゲージメント・システム)

**Status**: Phase Implementation Complete (2026-05-08)

### Drive SSoT (正本)
- **Narrative File**: `kondo_narrative_v1.16.md`
  - Drive ID: `1LsrD7u-Jd5Py1Qv2d3FkWe1oeUoFVwd-xhYaCM4y6TU`
  - Location: 専務理事対応（AI活用）/kondo_narrative_v1.16.md
  - Purpose: 全ツール（Code・Codex・Cowork）アクセス用 SSoT
  - Updated: 2026-05-08

### GitHub Mirror (ミラー・版管理・差分確認)
- `docs/pmo_engagement_template.md` - PMO 向けタスク説明テンプレート
- `docs/kondo_core_roles.md` - 5 つのコア・ロール定義
- `docs/llm_engagement_systemprompt.md` - LLM 向けシステムプロンプト

### Related Memory
- `memory/narrative_engagement_system.md` - 実装完了記録

### Architecture
```
Drive (SSoT: 正本)
  ↑↓ 同期
GitHub (Mirror: 版管理・差分確認)
```

**Purpose**: 近藤さんのモチベーション・活力向上
- タスク説明時に「意味・効果」を示唆
- 5 つのコア・ロールで役割発揮を可視化
- PMO・LLM が統一テンプレートで説明
"""

def get_oauth_credentials():
    """
    Get OAuth credentials using OAuth 2.0 flow.

    First attempts to use a stored refresh token.
    If not available, initiates OAuth flow for user authorization.
    """
    if not CREDENTIALS_FILE.exists():
        raise FileNotFoundError(
            f"Google OAuth credentials file not found: {CREDENTIALS_FILE}\n"
            "Please ensure ~/.claude/credentials.json contains valid OAuth client credentials."
        )

    # Load client credentials
    with open(CREDENTIALS_FILE, 'r') as f:
        client_config = json.load(f)

    # Check for stored OAuth token
    if OAUTH_TOKEN_FILE.exists():
        print(f"✓ Loading stored OAuth token from: {OAUTH_TOKEN_FILE}")
        creds = Credentials.from_authorized_user_file(
            str(OAUTH_TOKEN_FILE), SCOPES
        )

        # Refresh token if expired
        if creds.expired and creds.refresh_token:
            print("  Token expired, refreshing...")
            creds.refresh(Request())
            # Save refreshed token
            with open(OAUTH_TOKEN_FILE, 'w') as f:
                f.write(creds.to_json())

        return creds

    # No stored token, initiate OAuth flow
    print(f"✓ Initiating OAuth flow for Google Docs API")
    print(f"  Client config from: {CREDENTIALS_FILE}")

    flow = InstalledAppFlow.from_client_config(client_config, SCOPES)
    creds = flow.run_local_server(port=0)

    # Save token for future use
    with open(OAUTH_TOKEN_FILE, 'w') as f:
        f.write(creds.to_json())
    print(f"✓ OAuth token saved to: {OAUTH_TOKEN_FILE}")

    return creds

def update_manifest(check_only=False, dry_run=False):
    """Update MANIFEST with engagement system section.

    Args:
        check_only: If True, only verify without writing
        dry_run: If True, show what would happen without writing
    """
    print(f"📄 Updating MANIFEST document (ID: {MANIFEST_DOC_ID})")
    print(f"   Section: Issue #21 Engagement System Files")

    if check_only:
        print(f"   Mode: ✓ CHECK-ONLY (no changes to Drive)")
    if dry_run:
        print(f"   Mode: 🔍 DRY-RUN (preview only)")

    # Get OAuth credentials
    try:
        credentials = get_oauth_credentials()
    except Exception as e:
        print(f"❌ Failed to get OAuth credentials: {e}")
        raise

    # Build Docs API client
    service = build('docs', 'v1', credentials=credentials)

    # Check if section already exists (idempotency check - ROBUST)
    try:
        # ✅ NEW: Include tabs content for complete document structure
        doc = service.documents().get(
            documentId=MANIFEST_DOC_ID,
            includeTabsContent=True
        ).execute()

        # ✅ NEW: Collect content from both body and tabs
        contents = []

        # 1. Fallback: Traditional body.content (for non-tabbed documents)
        contents.extend(doc.get('body', {}).get('content', []))

        # 2. Main: Tabbed content (for modern tabbed documents)
        tabs = doc.get('tabs', [])
        detected_tab_id = None  # Store the first tab ID for insertion

        for tab_idx, tab in enumerate(tabs):
            if detected_tab_id is None:
                detected_tab_id = tab.get('tabId')  # Capture first tab ID

            document_tab = tab.get('documentTab', {})
            body = document_tab.get('body', {})
            contents.extend(body.get('content', []))

        # ✅ FIX: Robust section existence check: extract ALL text from unified content
        # NOTE: Google Docs API stores text in 'textRun.content', not 'textRun.text'
        full_doc_text = ''
        for element in contents:
            if 'paragraph' in element:
                # Extract all text runs from paragraph
                paragraph_text = ''.join([
                    run['textRun'].get('content', '')  # ← FIX: use 'content' not 'text'
                    for run in element['paragraph'].get('elements', [])
                    if 'textRun' in run
                ])
                full_doc_text += paragraph_text + '\n'
            elif 'table' in element:
                # Extract text from table cells
                table = element['table']
                for row in table.get('tableRows', []):
                    for cell in row.get('tableCells', []):
                        for cell_element in cell.get('content', []):
                            if 'paragraph' in cell_element:
                                cell_text = ''.join([
                                    run['textRun'].get('content', '')  # ← FIX: use 'content' not 'text'
                                    for run in cell_element['paragraph'].get('elements', [])
                                    if 'textRun' in run
                                ])
                                full_doc_text += cell_text + ' '

        # Check for section marker: "## 🎯 Issue #21: Engagement System Files"
        section_markers = [
            'Issue #21: Engagement System Files',
            'Issue #21 Engagement System Files',
            'Issue #21: Engagement'
        ]

        section_exists = any(marker in full_doc_text for marker in section_markers)

        # ✅ NEW: Debug information about detected structure
        print(f"\n📊 Document structure detected:")
        print(f"   - body.content elements: {len(doc.get('body', {}).get('content', []))}")
        print(f"   - Tabs found: {len(tabs)}")
        if tabs:
            print(f"   - First tab ID: {detected_tab_id}")
            for tab_idx, tab in enumerate(tabs):
                tab_content_count = len(tab.get('documentTab', {}).get('body', {}).get('content', []))
                print(f"   - Tab {tab_idx} content elements: {tab_content_count}")

        if section_exists:
            print(f"\n⏭️  Section 'Issue #21: Engagement System Files' already exists in document")
            print(f"   Document text contains: {[m for m in section_markers if m in full_doc_text]}")
            print(f"   Skipping insertion (idempotency check PASSED)")
            return {'status': 'skipped', 'reason': 'section_already_exists'}
        else:
            print(f"\n✅ Idempotency check: Section NOT found in document (safe to insert)")
    except Exception as e:
        print(f"⚠️  Warning: Could not fully verify existing content: {e}")
        print(f"   This is a BLOCKER - canceling insertion to prevent duplicates")
        return {'status': 'error', 'reason': f'idempotency_check_failed: {str(e)}'}

    # ✅ NEW: Check-only mode - verify without writing
    if check_only:
        print(f"\n✅ CHECK-ONLY mode: Section NOT found (safe to insert)")
        print(f"   Use without --check-only to actually insert")
        return {'status': 'check_only', 'reason': 'verified_safe_to_insert'}

    # ✅ NEW: Dry-run mode - show what would happen
    if dry_run:
        print(f"\n🔍 DRY-RUN mode:")
        print(f"   Would insert at index: 1")
        if detected_tab_id:
            print(f"   Would insert in tab: {detected_tab_id}")
        print(f"   Text length: {len(ENGAGEMENT_SYSTEM_SECTION)} characters")
        print(f"   Section length: ~20 lines")
        print(f"   Side effect: Drive MANIFEST would be modified")
        return {'status': 'dry_run', 'reason': 'would_insert_section'}

    # Prepare the request with ✅ NEW: explicit tabId
    location = {'index': 1}
    if detected_tab_id:
        location['tabId'] = detected_tab_id
        print(f"\n📍 Will insert into tab: {detected_tab_id}")

    requests = [
        {
            'insertText': {
                'text': ENGAGEMENT_SYSTEM_SECTION,
                'location': location
            }
        }
    ]

    # Execute the request
    try:
        result = service.documents().batchUpdate(
            documentId=MANIFEST_DOC_ID,
            body={'requests': requests}
        ).execute()

        print(f"\n✅ MANIFEST updated successfully")
        print(f"   Document ID: {MANIFEST_DOC_ID}")
        print(f"   Changes: {len(result.get('replies', []))} request(s) executed")
        print(f"\n📍 View document: https://docs.google.com/document/d/{MANIFEST_DOC_ID}/edit")
        print(f"\n📋 Verification needed:")
        print(f"   [ ] Open document and verify ONLY ONE 'Issue #21: Engagement System Files' section exists")
        print(f"   [ ] No duplicate sections present")
        print(f"   [ ] Run script again to confirm idempotency (status: skipped)")
        return result

    except Exception as e:
        print(f"\n❌ Failed to update MANIFEST: {e}")
        print(f"\n🛡️  SAFETY: Idempotency check prevented insertion.")
        print(f"   No changes were made to the document.")
        raise

if __name__ == '__main__':
    # ✅ NEW: Command-line argument parsing
    parser = argparse.ArgumentParser(
        description='Update MANIFEST document with Issue #21 Engagement System section',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  # Check if safe to insert (no Drive changes)
  python scripts/update_manifest.py --check-only

  # Preview what would happen (no Drive changes)
  python scripts/update_manifest.py --dry-run

  # Actually insert (requires idempotency check to pass)
  python scripts/update_manifest.py
        '''
    )

    parser.add_argument(
        '--check-only',
        action='store_true',
        help='Verify without writing to Drive'
    )

    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would happen without writing'
    )

    args = parser.parse_args()

    try:
        update_manifest(check_only=args.check_only, dry_run=args.dry_run)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        exit(1)
