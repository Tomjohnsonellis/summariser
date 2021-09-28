import streamlit as st
from blog_summariser import give_me_summary_and_stats

st.title("Blog Summariser")
st.write("Hello! This project makes use of Huggingface's powerful model to condense down lengthy blog posts")
url = st.text_input("Paste a blog url here")
if st.button("Summarise!"):
    st.write("Summarising...")
    text, res, stats = give_me_summary_and_stats(url)
    st.title("Summarised version:")
    for t in res:
        st.write(t["summary_text"])
    # st.write(text)
    st.title("Stats:")
    st.write(f"Original length: {stats['original_length']} ")
    st.write(f"Summary length: {stats['summary_length']} ")
    percentage = int(round(stats["summary_length"] / stats["original_length"] * 100, 0))
    st.write(f"Condesed to {percentage}% of original size!")
    st.write(f"You can read {stats['savings']} fewer characters!")
