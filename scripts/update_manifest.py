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

def update_manifest():
    """Update MANIFEST with engagement system section."""
    print(f"📄 Updating MANIFEST document (ID: {MANIFEST_DOC_ID})")
    print(f"   Section: Issue #21 Engagement System Files")

    # Get OAuth credentials
    try:
        credentials = get_oauth_credentials()
    except Exception as e:
        print(f"❌ Failed to get OAuth credentials: {e}")
        raise

    # Build Docs API client
    service = build('docs', 'v1', credentials=credentials)

    # Check if section already exists (idempotency check)
    try:
        doc = service.documents().get(documentId=MANIFEST_DOC_ID).execute()
        doc_content = doc.get('body', {}).get('content', [])

        # Check if "Issue #21: Engagement System Files" already exists
        section_exists = False
        for element in doc_content:
            if 'paragraph' in element:
                text = ''.join([
                    run.get('text', '')
                    for run in element['paragraph'].get('elements', [])
                    if 'textRun' in run
                ])
                if 'Issue #21' in text and 'Engagement System Files' in text:
                    section_exists = True
                    break

        if section_exists:
            print(f"\n⏭️  Section 'Issue #21: Engagement System Files' already exists")
            print(f"   Skipping insertion (idempotency check)")
            return {'status': 'skipped', 'reason': 'section_already_exists'}
    except Exception as e:
        print(f"⚠️  Warning: Could not verify existing content: {e}")
        print(f"   Proceeding with insertion attempt...")

    # Prepare the request
    requests = [
        {
            'insertText': {
                'text': ENGAGEMENT_SYSTEM_SECTION,
                'location': {
                    'index': 1  # Insert at the beginning
                }
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
        return result

    except Exception as e:
        print(f"\n❌ Failed to update MANIFEST: {e}")
        raise

if __name__ == '__main__':
    try:
        update_manifest()
    except Exception as e:
        print(f"\n❌ Error: {e}")
        exit(1)
