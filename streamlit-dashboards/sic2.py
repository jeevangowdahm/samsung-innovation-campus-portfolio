import streamlit as st 
import pandas as pd
d={
    "roll no":[101,102,103,104,105],
    "Name":['ramesh','devi','suresh','usha','hari']
}
df=pd.DataFrame(d)
st.write("Students details",df)
st.markdown("# display data frame")#Tittle
st.markdown("## Student Database")#header
st.markdown("### RNSIT")#Subheader
st.write("Students Details",df)
st.code("""import streamlit as st 
        import pandas as pd
        d={
            "roll no":[101,102,103,104,105],
            "Name":['ramesh','devi','suresh','usha','hari']
        }
""")