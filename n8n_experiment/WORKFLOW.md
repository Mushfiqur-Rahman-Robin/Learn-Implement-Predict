# n8n Expense Tracker with LLM Extraction and Error Handling

This n8n workflow provides a robust solution for tracking daily expenses directly from Telegram messages, leveraging a Large Language Model (LLM) for data extraction and integrating a dedicated error handling mechanism for reliability.

## 🚀 How it Works

The workflow automates the following steps:

1.  **Telegram Message Trigger:** Listens for incoming messages via a Telegram bot.
2.  **Timezone Adjustment:** Adjusts the timestamp of the incoming message to the Dhaka timezone.
3.  **LLM-Powered Data Extraction:** Sends the user's expense message to a local LLM (Ollama, specifically using the Gemma 3 model as configured) to intelligently extract the expense `amount` and `item`.
4.  **Data Structuring:** Processes the LLM's output and combines it with the adjusted date and time into a clean JSON object.
5.  **Google Sheets Integration:** Appends the extracted expense details (Date, Time, Amount, Item) to a designated Google Sheet.

### Error Handling

A separate, dedicated error handling workflow (not included in this JSON, but configured to work with it) is responsible for:

*   Catching any errors that occur at any stage of the main expense tracker workflow.
*   Sending an immediate and detailed notification to a specified Telegram chat, including the workflow name, execution ID, the node where the error occurred, and the error message.

## ✨ Features

*   **Telegram Integration:** Easily log expenses by sending a message to your bot.
*   **Timezone Correction:** Ensures all timestamps are consistent with Dhaka time.
*   **Intelligent Extraction:** Uses an LLM to flexibly parse expense details from natural language.
*   **Google Sheets Storage:** Centralized and organized storage for all your expense data.
*   **Robust Error Notifications:** Get instant alerts on Telegram if anything goes wrong, ensuring workflow reliability.

## 🛠️ Setup Instructions (High-Level)

To get this workflow running, you will need to:

1.  **Import this Workflow JSON:** Import this file into your n8n instance.
2.  **Telegram Credentials:**
    *   Create a Telegram bot using BotFather.
    *   Set up a `Telegram API` credential in n8n with your bot token.
    *   Replace `dummy_webhook_id` (if present) with a newly generated one (n8n usually handles this on activation).
3.  **Ollama Instance:**
    *   Have an Ollama instance running locally or on a reachable server.
    *   Ensure the `gemma3:270m` model is pulled and available (`ollama pull gemma3:270m`).
    *   Update the `HTTP Request to Ollama for Extraction` node's URL (`http://your_ollama_host:11434/api/generate`) to point to your actual Ollama host.
4.  **Google Sheets Credentials:**
    *   Set up a `Google Service Account` credential in n8n with access to your desired Google Sheet.
    *   Replace `dummy_google_sheet_id` with your Google Sheet's actual ID.
    *   Update `Your_Expenses_Sheet_Name` with the exact name of the sheet you want to use for expenses (e.g., "Expenses").
5.  **Error Handling Workflow (Crucial for Reliability!):**
    *   Create a separate n8n workflow for error handling (e.g., as described in previous conversations, using an "Error Trigger" and "Telegram" node).
    *   Ensure this error handling workflow is **Active**.
    *   In *this* workflow's settings (your expense tracker), configure the `Error Workflow` option to point to your active error handling workflow's ID (e.g., replace `dummy_error_workflow_id`).
6.  **Activate this Workflow:** Once configured, activate this `expense tracker workflow` by toggling the switch in the top right of its editor to "Active".

---

**Note:** This JSON has been sanitized to remove personal IDs, API keys, and specific environment details. You will need to configure your own credentials and replace placeholder values marked `dummy_...` or `your_...` after importing.