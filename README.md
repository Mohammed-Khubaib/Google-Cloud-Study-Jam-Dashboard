
# Google Cloud Study Jam (GCSJ) - GDSC MCET
## Dashboard
This repository contains the code for the Study Jam web application that helps you track progress, view the leader board, and more.

## Getting Started

### Prerequisites

Make sure you have the following Python packages installed:

- `datetime`
- `pytz`
- `json`
- `numpy`
- `pandas`
- `streamlit`
- `streamlit_lottie`
- `st_on_hover_tabs`
- `streamlit_elements`
- `streamlit_nivo`
- `streamlit_on_Hover_tabs`
- `st_gsheets_connection`

You can install these packages using `pip`:

```bash
pip install -r requirements.txt
```

## Repository Structure
```
.
├── app.py
├── redemption.py
├── lineChart.py
├── pieChart.py
├── ProgressBar.py
├── SheetsConnection.py(optional to use)
├── SubHeadingText.py
├── GetData.py
├── requirements.txt
├── style.css
├── assets
│   ├── GCSJ.mov
│   ├── GD.json
│   ├── GDSC.json
│   ├── GDSC_DASHBOARD.mov
│   ├── GLoading.json
│   ├── gcsj.png
│   ├── gcsj_black.png
│   ├── img2.png
│   └── logo.png
├── GcsjData
│   ├── 1.csv
.   .
.   .
.   .
│   │
│   └── 30.csv
```

---
### Required Changes :
- Replace the url link with your own public Google Sheets Link \
`SheetsConnection.py`
```python
from streamlit_gsheets import GSheetsConnection
import streamlit as st

def File():
    url = "your public Google Sheets Url"
    conn = st.gcsheets(key=url)
    file = conn.read(usecols=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    return file
```

## Deployment

The web application is live and can be accessed [here](https://gdscmcet.streamlit.app/). Feel free to explore and use the app to track participant progress and view the leader board.

<!--### Web app Preview :
[Google Cloud Study Jam Video](https://github.com/Mohammed-Khubaib/GDSC_MCET/assets/102320167/ca94a6c8-3575-4271-b7b2-331dd229de68)-->



