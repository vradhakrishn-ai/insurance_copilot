# WithYou Insurance — Assistant

This repository contains a Streamlit-based insurance assistant for WithYou Insurance. The assistant answers product questions, provides premium guidance, and enforces safety guardrails to block PII/HCI and prompt-injection attempts.

## Files
- `ins_cop.py`: Main Streamlit app and assistant logic.
- `data/products.json`: Static product metadata used by the assistant.
- `data/blocked_terms.json`: Blocked terms (PII/HCI and unsafe keywords).
- `evaluate.py`: Evaluation harness that runs 20 simulated queries and outputs `reports/evaluation_report.md`.
- `reports/`: Generated evaluation reports.

## Setup
1. Create a Python environment and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Create a `.env` file with your OpenAI API key if you intend to run live LLM calls. The evaluation script `evaluate.py` does not call the external API.

## Run the app

```bash
streamlit run ins_cop.py
```

The UI includes optional structured fields for `Age`, `Gender`, and `Country` which are validated (age 18-99, gender in Male/Female/Other, country must be India). If validation fails, the assistant will politely decline and provide the support contact.

## Evaluation

To run the built-in evaluation which simulates 20 queries and checks guardrails:

```bash
python evaluate.py
```

Results are written to `reports/evaluation_report.md`.

## Support
For requests involving PII or highly confidential information, the assistant redirects users to contact support:

- Phone: +91 00000 00000
- Email: support@withyouinsurance.in

