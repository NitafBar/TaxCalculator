import streamlit as st

st.title('Tacs')

# Stage 1
st.header("Stage 1")
st.caption("Assessable Income")
txtAI = st.text_input("AI", value = 0, key = "AI", label_visibility="hidden")

st.caption("Allowable Deductions")
txtAD = st.text_input("AD", value = 0, key = "AD", label_visibility="hidden")

# Stage 2
st.header("Stage 2")
st.subheader("Taxable Income")
TI = float(txtAI) - float(txtAD)
st.text(TI)

st.subheader("Tax Amount")

def taxRate():

	if (float(txtAI) - float(txtAD)) <= 18200:
		return 0

	elif (float(txtAI) - float(txtAD)) >= 18201 and (float(txtAI) - float(txtAD)) <= 45000:
		return (float(TI) - 18200) * 0.19

	elif (float(txtAI) - float(txtAD)) >= 45001 and (float(txtAI) - float(txtAD)) <= 120000:
		return (float(TI) - 45000) * 0.325 + 5092

	elif (float(txtAI) - float(txtAD)) >= 120001 and (float(txtAI) - float(txtAD)) <= 180000:
		return (float(TI) - 120000) * 0.37 + 29467

	elif (float(txtAI) - float(txtAD)) >= 180001:
		return (float(TI) - 180000) * 0.45 + 51666

st.text(taxRate())

# Stage 3
st.header("Stage 3")
st.caption("Tax Offset")
txtTO = st.text_input("TO", value = 0, key = "TO", label_visibility="hidden")

st.subheader("New Tax Amount")

NTA = taxRate() - float(txtTO)
st.text(NTA)

# Stage 4
st.header("Stage 4")
st.caption("Credit")
credit = st.text_input("credit", value = 0, key = "credit", label_visibility="hidden")

st.subheader("Final Tax Amount")

st.text( NTA + (TI * 0.02) - float(credit))

