import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as mtick

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

# Convert Volume to Millions
bridge_df["volumeMillionsUSD"] = bridge_df["volumeUSD"] / 1_000_000

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





# Load Bridging Data
bridging_data = [
    {"bridgeType": "Native Canonical Bridge", "token": "ETH", "volumeUSD": 981836.96},
    {"bridgeType": "Hyperlane", "token": "SOL", "volumeUSD": 72941.47},
    {"bridgeType": "Hyperlane", "token": "BONK", "volumeUSD": 3047.94}
]

# Convert to DataFrame
bridge_df = pd.DataFrame(bridging_data)

# Streamlit App
st.title("SOON Network Bridging Inflows")

st.header("🔗 Bridging Inflows by Token (in Thousands USD)")

# Create a bar chart
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(x="token", y="volumeUSD", hue="bridgeType", data=bridge_df, ax=ax)

# Update axis labels
ax.set_ylabel("Total Volume (Thousands USD)")
ax.set_xlabel("Token")
ax.set_title("Bridging Inflows to SOON Network (in Thousands USD)")

# Format the y-axis to display values in thousands
ax.yaxis.set_major_formatter(mtick.FuncFormatter(lambda x, _: f"{x/1_000:,.0f}K"))

# Display the chart in Streamlit
st.pyplot(fig)

# Display Updated Table in Streamlit
st.write("### Raw Bridging Data (Volume in USD)")
st.dataframe(bridge_df[["bridgeType", "token", "volumeUSD"]])