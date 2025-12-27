import streamlit as st


def is_number(num):
    return num.isdigit()


def validation(num):
    first_checksum = 0
    second_checksum = 0

    for i in range(len(num)-1, -1, -1):
        tmp_digit = int(num[i])
        if i & 1:
            first_checksum += tmp_digit
            tmp_digit *= 2
            second_checksum += (tmp_digit // 10 + tmp_digit % 10)
        else:
            second_checksum += tmp_digit
            tmp_digit *= 2
            first_checksum += (tmp_digit // 10 + tmp_digit % 10)

    return (first_checksum % 10 == 0 or second_checksum % 10 == 0) and len(num) >= 13


def get_card_brand(num):
    # American Express: starts with 34 or 37, length 15
    if num[0] == '3' and num[1] in ['4', '7'] and len(num) == 15:
        return "AMEX"
    # Mastercard: starts with 51-55 or 2221-2720, length 16
    elif num[0] == '5' and int(num[1]) in range(1, 6) and len(num) == 16:
        return "MASTERCARD"
    elif num[:4].isdigit() and 2221 <= int(num[:4]) <= 2720 and len(num) == 16:
        return "MASTERCARD"
    # Visa: starts with 4, length 13, 16, or 19
    elif num[0] == '4' and len(num) in [13, 16, 19]:
        return "VISA"
    # Discover: starts with 6011, 622126-622925, 644-649, or 65, length 16-19
    elif len(num) >= 16 and len(num) <= 19:
        if num[:4] == '6011':
            return "DISCOVER"
        elif num[:6].isdigit() and 622126 <= int(num[:6]) <= 622925:
            return "DISCOVER"
        elif num[:3].isdigit() and 644 <= int(num[:3]) <= 649:
            return "DISCOVER"
        elif num[:2] == '65':
            return "DISCOVER"
    # Diners Club: starts with 300-305, 36, or 38, length 14
    elif len(num) == 14:
        if num[:3].isdigit() and 300 <= int(num[:3]) <= 305:
            return "DINERS CLUB"
        elif num[:2] in ['36', '38']:
            return "DINERS CLUB"
    # JCB: starts with 3528-3589, length 16-19
    elif num[:4].isdigit() and 3528 <= int(num[:4]) <= 3589 and len(num) >= 16 and len(num) <= 19:
        return "JCB"
    # UnionPay: starts with 62, length 16-19
    elif num[:2] == '62' and len(num) >= 16 and len(num) <= 19:
        return "UNIONPAY"
    else:
        return "INVALID"


st.set_page_config(page_title="Credit Card Validator", page_icon="💳",
                   layout="centered", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    html, body, [data-testid="stAppViewContainer"], .main {
        background: linear-gradient(135deg, #1a202c 0%, #2d3748 100%) !important;
    }
    
    .main {
        background: linear-gradient(135deg, #1a202c 0%, #2d3748 100%) !important;
        padding: 0 !important;
        min-height: 100vh;
    }
    
    .block-container {
        padding-top: 3rem !important;
        padding-bottom: 3rem !important;
        max-width: 600px !important;
        background: transparent !important;
    }
    
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #1a202c 0%, #2d3748 100%) !important;
    }
    
    [data-testid="stHeader"] {
        background: transparent !important;
    }
    
    section[data-testid="stSidebar"] {
        background: linear-gradient(135deg, #1a202c 0%, #2d3748 100%) !important;
    }
    
    .main > div {
        background: transparent !important;
    }
    
    [data-testid="stVerticalBlock"] {
        background: transparent !important;
    }
    
    [data-testid="stHorizontalBlock"] {
        background: transparent !important;
    }
    
    .element-container {
        background: transparent !important;
    }
    
    iframe {
        background: transparent !important;
    }
    
    .card-container {
        background: white;
        border-radius: 20px;
        padding: 3rem 2rem;
        box-shadow: 0 20px 60px rgba(0,0,0,0.3);
        margin: 2rem 0;
    }
    
    .title-container {
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .main-title {
        color: #2d3748;
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    
    .subtitle {
        color: #718096;
        font-size: 1rem;
        font-weight: 400;
    }
    
    .card-icon {
        font-size: 3.5rem;
        margin-bottom: 1rem;
    }
    
    .stTextInput > div > div > input {
        font-size: 1.3rem !important;
        padding: 1rem !important;
        border-radius: 12px !important;
        border: 2px solid #e2e8f0 !important;
        text-align: center;
        letter-spacing: 2px;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #667eea !important;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1) !important;
    }
    
    .stSuccess {
        background: linear-gradient(135deg, #48bb78 0%, #38a169 100%) !important;
        color: white !important;
        font-size: 1.3rem !important;
        padding: 1.5rem !important;
        border-radius: 12px !important;
        border: none !important;
        text-align: center;
        font-weight: 600;
        box-shadow: 0 4px 14px rgba(72, 187, 120, 0.4);
    }
    
    .stError {
        background: linear-gradient(135deg, #f56565 0%, #e53e3e 100%) !important;
        color: white !important;
        font-size: 1.3rem !important;
        padding: 1.5rem !important;
        border-radius: 12px !important;
        border: none !important;
        text-align: center;
        font-weight: 600;
        box-shadow: 0 4px 14px rgba(245, 101, 101, 0.4);
    }
    
    .stWarning {
        background: linear-gradient(135deg, #ed8936 0%, #dd6b20 100%) !important;
        color: white !important;
        font-size: 1.1rem !important;
        padding: 1rem !important;
        border-radius: 12px !important;
        border: none !important;
        text-align: center;
        font-weight: 600;
        box-shadow: 0 4px 14px rgba(237, 137, 54, 0.4);
    }
    
    .supported-cards {
        margin-top: 2rem;
        padding-top: 2rem;
        border-top: 2px solid #e2e8f0;
        text-align: center;
    }
    
    .supported-cards-title {
        color: #718096;
        font-size: 0.9rem;
        font-weight: 600;
        margin-bottom: 1rem;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .card-brands {
        display: flex;
        justify-content: center;
        gap: 1.5rem;
        flex-wrap: wrap;
    }
    
    .brand-badge {
        background: #f7fafc;
        padding: 0.5rem 1rem;
        border-radius: 8px;
        font-weight: 600;
        color: #4a5568;
        font-size: 0.85rem;
        border: 2px solid #e2e8f0;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<div class="card-container">', unsafe_allow_html=True)

st.markdown("""
    <div class="title-container">
        <div class="card-icon">💳</div>
        <h1 class="main-title">Card Validator</h1>
        <p class="subtitle">Verify your credit card number instantly</p>
    </div>
""", unsafe_allow_html=True)

num = st.text_input(
    "Card Number", "", placeholder="Enter card number", label_visibility="collapsed")

if num:
    # Remove spaces from the input
    num_cleaned = num.replace(" ", "")

    if is_number(num_cleaned):
        if validation(num_cleaned):
            result = get_card_brand(num_cleaned)
            if result == "INVALID":
                st.error("❌ INVALID CARD")
            else:
                st.success(f"✅ Valid {result} Card")
        else:
            st.error("❌ INVALID CARD")
    else:
        st.warning("⚠️ Please enter numbers only")

st.markdown("""
    <div class="supported-cards">
        <div class="supported-cards-title">Supported Cards</div>
        <div class="card-brands">
            <span class="brand-badge">VISA</span>
            <span class="brand-badge">MASTERCARD</span>
            <span class="brand-badge">AMEX</span>
            <span class="brand-badge">DISCOVER</span>
            <span class="brand-badge">DINERS CLUB</span>
            <span class="brand-badge">JCB</span>
            <span class="brand-badge">UNIONPAY</span>
        </div>
    </div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
