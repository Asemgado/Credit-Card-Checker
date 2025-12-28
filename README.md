# Online Credit Card Checker

#### Video Demo: <https://youtu.be/Zqrs9ngPg1M>

#### Live Demo: <https://credit-card-checker.streamlit.app/>

#### Description

Online Credit Card Checker is a compact, open-source Streamlit app and Python utility for detecting payment card networks (Visa, Mastercard, American Express, Discover, JCB, Diners Club, UnionPay, and others) from numeric prefixes and validating card numbers using the Luhn checksum. The project focuses on correctness, clarity, and privacy — making it suitable for demos, education, quick QA checks, and local testing.

Overview

- Purpose: provide an easy-to-run tool that helps developers, testers, and instructors demonstrate how card numbers are formatted and how basic validation works without handling or persisting real cardholder data.
- Audience: developers, QA engineers, educators, and hobbyists learning about payment card formats.

How it works

- Brand detection: the app checks prefix ranges and card length to infer the issuing network (e.g., Visa numbers start with `4`, American Express use `34`/`37`, Mastercard includes ranges `51–55` and `2221–2720`).
- Validation: uses the Luhn algorithm (mod-10 checksum) to detect common typos and invalid numbers. The algorithm is implemented in `main.py` and runs client-side inside the Streamlit app.

Supported card networks

- VISA, MASTERCARD, AMEX (American Express), DISCOVER, DINERS CLUB, JCB, UNIONPAY

Implementation details

- Language: Python 3.8+
- UI framework: Streamlit (single-file UI in `main.py`)
- Key functions: `get_card_brand()` (prefix/length detection) and `validation()` (Luhn checksum).
- Styling: custom CSS is injected in the app for a compact, modern card-style interface.

User interface

- Single input field for card number (spaces are ignored). The UI displays immediate color-coded feedback: valid (success), invalid (error), or non-numeric input (warning).
- A small supported-cards panel lists the networks the app recognizes.

Security & privacy

- The app performs all validation locally in the browser/Streamlit process — no card numbers are sent to external services.
- This project is intended for educational/testing purposes only. It is not PCI-compliant and should never be used as-is to collect, store, or transmit real cardholder data.

Use cases

- Teaching how the Luhn algorithm and card BIN ranges work
- Quick local validation during development and QA
- Demoing a small Streamlit app and simple client-side validation logic

Files of interest

- `main.py`: single-file Streamlit application containing UI, validation logic, and styling.

Contributing

- Contributions, bug reports, and improvements are welcome. Please open issues or pull requests on the repository.

Features

- Detects common card types by number prefix and length
- Validates card numbers with the Luhn checksum
- Simple, responsive Streamlit UI for quick testing
- Lightweight and easy to run locally or deploy

Quick start

1. Install dependencies (requires Python 3.8+):

 pip install streamlit

2. Run the app:

 streamlit run main.py

Notes

- This tool is for educational and testing purposes only. Do not use it to store or transmit real cardholder data in insecure ways.
- Contributions and improvements are welcome.
