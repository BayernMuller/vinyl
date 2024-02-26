<span align="center">
    <img src="docs/preview.png"/>
</span>

<span align="center">

# vinyl

</span>

<p align="center">
    <img src="https://img.shields.io/github/forks/BayernMuller/vinyl?style=plastic"/>
    <img src="https://img.shields.io/github/license/BayernMuller/vinyl?style=plastic"/>
</p>


### What is vinyl?

* vinyl is a streamlit template for managing your records collection.

### How to setup?

* [Fork](https://github.com/BayernMuller/vinyl/fork) this repository.
* Clone your forked repository and install requirements.
```bash
git clone https:://github.com/<your-username>/vinyl
cd vinyl
pip install -r requirements.txt
```
* Add `list.json` file on the root of the project with the following structure:
```json
[
    {
        "cover": "https://<cover_url>",
        "artist": "The Beatles",
        "title": "Sgt. Pepper's Lonely Hearts Club Band",
        "genre": "Psychedelic Rock",
        "format": "LP",
        "country": "UK",
        "year": 1967,
    },
    {
        "cover": "https://<cover_url>",
        "artist": "Black Sabbath",
        "title": "Master of Reality",
        "genre": "Heavy Metal",
        "format": "LP",
        "country": "UK",
        "year": 1971,
    },
    ...
]
```
* You can see the example of `list.json` file [here](https://github.com/BayernMuller/vinyl/blob/jayden/records/list.json).


### Publish your collection
* You can publish your collection using [Streamlit Sharing](https://share.streamlit.io/).
* Push your changes to your forked repository and deploy your app on Streamlit Sharing.
* Demo app is deployed here: https://record.streamlit.app.
