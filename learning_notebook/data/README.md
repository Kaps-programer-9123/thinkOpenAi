## Additional Clarification (for Handbook or README)

**Why this matters:**
The `.env` file helps you separate configuration (like your API credentials) from your code. It’s especially important because:

* It keeps keys out of version control for security.
* It lets students easily swap their own API key without modifying code.
* It removes confusion about file paths or variable names.

**Example `.env` content:**

```env
OPENROUTER_BASE_URL="https://openrouter.ai/api/v1"
OPENROUTER_API_KEY="paste-your-key-here"
```

**Key generation workflow:**

1. Go to **[openrouter.ai](https://openrouter.ai/google/gemini-2.0-flash-exp:free)** → sign in
2. Visit the **API Keys** section
3. Click **Create New Key** → name it (e.g., “Workshop Key”)
4. (Optional) Set a credit limit
5. Click **Generate** → copy the API key
6. Paste into the `.env` file under the `OPENROUTER_API_KEY` line
7. Save the file and rerun your code.

---
