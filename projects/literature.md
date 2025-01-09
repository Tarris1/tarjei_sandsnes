# Lectura: a better way to discover literature!

Discovering and managing literature is an integral part of any reader's life.  How can I ensure that I have control over the books I want to read, the books I own, the books that I have read? How can I find books that may knock out my absolute favorites? Perhaps an obscure 17th century author from a region you have never explored will fill this need? Perhaps you were not aware that Marcel Proust wrote a lengthy book prior to his infamous *In Search of Lost Time* during which he experimented with his novel *stream of consciousness* style? With this platform, I aim to answer all (and any other you may have surrounding litterature) of these questions!

---

## Technology Stack:
- Front-end written in **React.JS**, necessarily supplemented with **HTML** and **CSS**
- Back-end: **Python** (API through **fastAPI**, data handling via **Pandas**, **Numpy**, etc.), **PostgreSQL** (database management), and **SPARQL** (RDF query language connecting to Wikipedia's database Wikidata, queried via Python and stored in my PostgreSQL database)
- **Deployment TBA**

---

### Key Metrics:
- **Authors available with a text attached**: 60,868
- **Total amount of authors**: 791,773
- **#Texts available**: 295,648

---

### Main Challenges:

1. **Using the best data source**: There is an endless amount of available data sources for litterature, some substantially larger than others. Throughout my initial investigations, I stumbled upon several that were open source and ridiculously large, but by digging through it, I discovered that the data quality is severely lacking, making them difficult if not impossible sources to work with. I finally opted for using Wikidata for multiple reasons:
    i. It is the database of Wikipedia, data used by people from all over the world, and covers all kinds of people.
    ii. It is open source and maintained by volunteers. This allows for continuous updating and quality assurance (although adjustments may be erroneous).
    iii. Data can be and is usually provided with a specific source that can also be extracted for additional validation (especially useful in case there are alternative values).
    iv. Data is language-tagged, allowing for more accurate translations.
2. **Incomplete data**: A significant amount of authors obtained from Wikiedia do not have texts attached to them, and a significant amount of authors with texts attached to them are incomplete. This is especially true for older litterature or more obscure authors. Inversely, it does occur that authors have duplicate data (such as poetry collections and individual poems appearing separately), but that is handled automatically on my website.
- I plan to supplement text data from other sources (i.e. ISNI), which will be fed back to Wikidata
3. **Data Quality assurance**: Many data validation techniques are automated before being displayed to the user. It is difficult, however, to ensure that adjustments are accurate.
- I plan to attach data sources when available to data points into the system, to further support the user's confidence

---

### Visualizations:
Examples of how the platform looks like at the moment:

![Homepage](https://raw.githubusercontent.com/Tarris1/tarjei_sandsnes/refs/heads/main/projects/homepage.png)
![Listspage](https://raw.githubusercontent.com/Tarris1/tarjei_sandsnes/refs/heads/main/projects/lists.png)
---

### Links:
- [GitHub Repository](https://github.com/Lecturaorg)