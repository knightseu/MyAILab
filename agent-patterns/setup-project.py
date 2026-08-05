 # 🎓 WORKSHOP ONLY — run this INSTEAD of the AI Studio key cell below.
# Prereq: claim your credit first, using the SAME Google account you sign in with here.
import os, subprocess, sys, time

PROJECT_ID = ""            # leave blank to create one automatically
LOCATION   = "us-central1"
MODEL      = "gemini-2.5-flash"   # gemini-flash-latest is an AI-Studio-only alias

from google.colab import auth
auth.authenticate_user()                          # also authenticates the gcloud CLI
…                    "   → This isn't the usual propagation delay — read the error above.")
            raise SystemExit(
                f"\n✋ Vertex AI won't answer on {PROJECT_ID}.\n"
                f"   {type(e).__name__}: {str(e)[:300]}\n{hint}"
            )
        print(f"   waiting for Vertex AI to come up on the new project… ({attempt * 10}s)",
              flush=True)
        time.sleep(10)

print(f"\n✅ Vertex AI on {PROJECT_ID} · {LOCATION} · {MODEL} — answered a test call", flush=True)