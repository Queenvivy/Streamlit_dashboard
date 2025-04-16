import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(layout="wide")
st.title("Solana Transaction Analysis Dashboard")


CSV_URL = "https://raw.githubusercontent.com/Queenvivy/Solana-dashboard/main/dune%20solana%20transaction.csv"
df = pd.read_csv(CSV_URL)

    # === Chart 1: Wasted Capacity Pie Chart ===
    st.subheader("1. Solana Network Efficiency: Wasted Capacity")
    labels = ['Successful TXs (57%)', 'Failed TXs (43%)']
    sizes = [57, 43]
    colors = ['#00FFA3', '#FF4D4D']

    fig1, ax1 = plt.subplots(figsize=(6, 6))
    ax1.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%',
            startangle=90, textprops={'fontsize': 12})
    ax1.set_title("Solana Network Efficiency: Wasted Capacity (30-Day Avg)", fontsize=14)
    st.pyplot(fig1)

    st.markdown("""
    **Network Efficiency Loss**

    **What it shows:** 43% of Solana’s capacity wasted on failed transactions.  
    **Key insight:** Nearly half the network’s throughput is useless.  
    **Why it matters:** Explains why real users experience slow performance despite high TPS claims.
    """)

    # === Chart 2: Projected Failure Rates After Fixes ===
    st.subheader("2. Projected Failure Rates After Proposed Fixes")
    labels = ['Current Model', 'With Dynamic Fees', 'With Rate Limits']
    failure_rates = [43, 15, 8] 
    fig2, ax2 = plt.subplots(figsize=(8, 5))
    bars = ax2.bar(labels, failure_rates, color=['#FF4D4D', '#FFA500', '#00FFA3'])
    ax2.set_ylabel("Failure Rate (%)")
    ax2.set_ylim(0, 50)
    ax2.set_title("Projected Failure Rates After Proposed Fixes", fontsize=14)
    ax2.grid(axis='y', alpha=0.3)
    for bar in bars:
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height, f'{height}%', ha='center', va='bottom')
    st.pyplot(fig2)

    st.markdown("""
    **Projected Impact of Fixes**

    **What it shows:** Hypothetical reduction in failures with solutions:  
    - Current: 43% failures  
    - With dynamic fees: ~15%  
    - With rate limits: ~8%  

    **Key insight:** Small economic tweaks could cut failures by 4–5x.  
    **Why it matters:** Solutions are feasible without sacrificing affordability.
    """)

    # === Chart 3: Daily Failure Rate Over Time ===
    st.subheader("3. Daily Transaction Failure Rates")
    fig3, ax3 = plt.subplots(figsize=(10, 5))
    ax3.plot(df['block_date'], df['failure_rate_percentage'], marker='o', color='#9945FF', linewidth=2)
    ax3.axhline(y=43, color='red', linestyle='--', label='Average (43%)')
    ax3.set_title("Solana Daily Transaction Failure Rates (March 7 - April 6, 2025)", fontsize=14)
    ax3.set_xlabel("Date")
    ax3.set_ylabel("Failure Rate (%)")
    ax3.set_ylim(30, 50)
    ax3.legend()
    ax3.grid(axis='y', alpha=0.3)
    ax3.tick_params(axis='x', rotation=45)
    st.pyplot(fig3)

    st.markdown("""
    **Failure Rate Over Time**

    **What it shows:** Daily failure rates (34.9% to 48.8%) over 30 days.  
    **Key insight:** Failure rates are consistently high, spiking during NFT/memecoin events (e.g., March 29: 48.8%).  
    **Why it matters:** Proves failures are systemic, not temporary.
    """)

    # === Show Raw Data (optional) ===
    st.subheader("Raw Data")
    st.dataframe(df)
else:
    st.info("📂 Please upload the Solana CSV file to view the dashboard.")
