import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data (Manually Enter Your Data or Load from CSV)
testnet_data = {
    "totalTxCount": 1782395,
    "activeAddresses24h": 82,
    "activeAddresses7d": 1642
}

mainnet_data = {
    "totalTxCount": 250242,
    "totalAddressCount": 1019,
    "totalProgramCount": 37,
    "activeAddresses24h": 40,
    "activeAddresses7d": 183
}

bridging_data = [
    {"bridgeType": "Native Canonical Bridge", "token": "ETH", "volumeUSD": 981836.96},
    {"bridgeType": "Hyperlane", "token": "SOL", "volumeUSD": 72941.47},
    {"bridgeType": "Hyperlane", "token": "BONK", "volumeUSD": 3047.94}
]

# Convert to DataFrames
mainnet_df = pd.DataFrame([mainnet_data])
testnet_df = pd.DataFrame([testnet_data])
bridge_df = pd.DataFrame(bridging_data)

# Streamlit App
st.title("SOON Network Data Analytics")

# Section 1: Summary Statistics
st.header("📊 Summary Statistics")
st.write("### Mainnet Data")
st.dataframe(mainnet_df)

st.write("### Testnet Data")
st.dataframe(testnet_df)

# Section 2: Transaction Volume Comparison
st.header("📈 Transaction Volume Comparison")

fig, ax = plt.subplots()
ax.bar(["Testnet", "Mainnet"], [testnet_data["totalTxCount"], mainnet_data["totalTxCount"]], color=["blue", "green"])
ax.set_ylabel("Total Transactions")
ax.set_title("Total Transactions on Testnet vs. Mainnet")
st.pyplot(fig)

# Section 3: Active Addresses Over 7 Days
st.header("👥 Active Users (Last 7 Days)")

fig, ax = plt.subplots()
ax.bar(["Testnet", "Mainnet"], [testnet_data["activeAddresses7d"], mainnet_data["activeAddresses7d"]], color=["orange", "red"])
ax.set_ylabel("Active Users (7 days)")
ax.set_title("Active Users: Testnet vs. Mainnet")
st.pyplot(fig)

# Section 4: Bridging Data
st.header("🔗 Bridging Statistics")
st.write("Bridge Transaction Volume (USD)")

# Create Bar Plot
fig, ax = plt.subplots()
sns.barplot(x="token", y="volumeUSD", hue="bridgeType", data=bridge_df, ax=ax)
ax.set_ylabel("Total Volume (USD)")
ax.set_title("Bridging Activity to SOON Network")
st.pyplot(fig)

st.write("### Raw Bridging Data")
st.dataframe(bridge_df)
