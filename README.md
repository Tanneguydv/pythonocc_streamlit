# pythonocc_streamlit
a way to interact with pythonocc webbrowser display with streamlit

### Installation

Prerequisites:

1. streamlit:  https://github.com/leon-thomm/Ryven
2. pythonocc-core: https://anaconda.org/conda-forge/pythonocc-core

```
# first create an environment
conda create --name=pyoccenv python=3.9
source activate pyoccenv  /alternate command/ conda activate pyoccenv
conda install -c conda-forge pythonocc-core=7.7.0
pip install streamlit
```

### Usage

In your terminal, with your conda env activate, just type:
```
streamlit run path_to_your_file/example_streamlit_pythonocc.py
```

### Examples

Here a small example of application: 

![screenshot_1](https://user-images.githubusercontent.com/81742654/219937113-603adc29-e2c0-4d50-9860-ced6637f2fef.png)
![screenshot_2](https://user-images.githubusercontent.com/81742654/219937130-0b8125c9-9257-4a9f-98fb-2417cea7385e.png)
