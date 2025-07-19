import streamlit as st

# Initialize session state
if "names" not in st.session_state:
    st.session_state.names = []

def main():
    st.set_page_config(page_title="Name Length Viewer", layout="centered")
    st.title("👤 5 Names Length Checker")

    # Only show input until 5 names are entered
    if len(st.session_state.names) < 5:
        st.markdown(f"### Enter Name {len(st.session_state.names) + 1} of 5")

        name_input = st.text_input("Enter a name:", key=f"name_input_{len(st.session_state.names)}")

        if st.button("Submit", key=f"submit_button_{len(st.session_state.names)}"):
            name = name_input.strip()
            if name:
                st.session_state.names.append(name)
                st.rerun()
            else:
                st.warning("⚠️ Please enter a valid name.")

    # Show results as names are added
    if st.session_state.names:
        st.markdown("### ✅ Name Length Results:")
        for idx, name in enumerate(st.session_state.names, 1):
            st.write(f"{idx}. **{name}** → {len(name)} characters")

    # Show reset button after 5 names
    if len(st.session_state.names) == 5:
        st.success("🎉 All 5 names entered!")
        if st.button("🔄 Reset"):
            st.session_state.names = []
            st.rerun()

if __name__ == "__main__":
    main()
