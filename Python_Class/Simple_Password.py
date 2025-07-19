import streamlit as st

# Function to check basic password validity
def is_valid_password(password: str, min_length: int = 8) -> bool:
    return len(password) >= min_length

# Main Streamlit app
def main():
    st.set_page_config(page_title="Simple Password Checker", layout="centered")
    st.title("🔐 Simple Password Checker")

    st.markdown("Enter a password to check if it meets the minimum length requirement.")

    password = st.text_input("Enter Password", type="password")
    min_length = st.slider("Minimum Length Required", 4, 20, 8)

    if st.button("Check Password"):
        if is_valid_password(password, min_length):
            st.success("✅ Password is valid!")
        else:
            st.error(f"❌ Password must be at least {min_length} characters long.")

    # Password example suggestions
    st.markdown("---")
    st.markdown("### 💡 Examples of Strong Passwords")
    st.markdown(
        """
        Here are a few examples of strong passwords that you can take inspiration from:
        - `S3cur3P@ss2025!`
        - `My_Dog$RunsFast99`
        - `!Ch3ck_Th1s_Out#`
        - `Purple&Tiger_8823`
        """
    )
    st.info("Tip: Use a mix of uppercase, lowercase, numbers, and symbols to create a strong password.")

if __name__ == "__main__":
    main()
