# Movie Recommender System

## Projektbeskrivelse
Udvikle et hybrid movie recommender system der kombinerer collaborative filtering og content-based filtering til at give personaliserede film anbefalinger. Systemet skal kunne trænes på historiske ratings data og give præcise anbefalinger baseret på brugerens tidligere præferencer.

## Succeskriterier
Projektet anses for færdigt når:
- Systemet kan give 10 film anbefalinger til en given bruger
- Root Mean Square Error (RMSE) < 1.0 på test datasættet
- En fungerende prototype med simpel web interface eller CLI
- Dokumentation der forklarer modellens funktion og ydeevne
- Minimum 3 forskellige recommendation algoritmer er sammenlignet

## Deadline
**Færdiggørelse: [INDSÆT DATO]**

## Stakeholders
- Mig selv (læring og portfolio)
- Potentielle arbejdsgivere (portfolio piece)
- [Tilføj eventuelle andre - underviser, studiegruppe, etc.]

## Ressourcepersoner
- Online communities: r/MachineLearning, Stack Overflow
- Kaggle kernels og diskussioner om recommender systems
- Research papers: "Matrix Factorization Techniques for Recommender Systems" (Koren et al.)
- [Tilføj mentor/underviser hvis relevant]

## Datasæt
**Primært datasæt:** MovieLens (https://grouplens.org/datasets/movielens/)
- MovieLens 100K (mindre, hurtigere til prototyping)
- MovieLens 25M (større, til final model)

**Supplementary data (optional):**
- IMDB metadata (genre, directors, actors)
- TMDB API for movie posters og beskrivelser

---

## Delmål

### Delmål 1: Data Exploration & Preprocessing (Uge 1)
**Status:** ⬜ Ikke startet

**Opgaver:**
- [ ] Download MovieLens dataset
- [ ] Exploratory Data Analysis (EDA) i Jupyter notebook
- [ ] Forstå data struktur: users, movies, ratings, timestamps
- [ ] Håndter missing values og outliers
- [ ] Train/validation/test split (70/15/15)
- [ ] Baseline statistik (gennemsnitlig rating, populære film)

**Færdig når:** EDA notebook er komplet med visualiseringer og data er splittet korrekt.

---

### Delmål 2: Baseline Model (Uge 1-2)
**Status:** ⬜ Ikke startet

**Opgaver:**
- [ ] Implementer simple baseline: gennemsnitlig rating
- [ ] Implementer popularity-based recommender
- [ ] Evaluér baseline models (RMSE, MAE)
- [ ] Dokumenter baseline performance

**Færdig når:** Baseline RMSE er beregnet og dokumenteret som reference point.

---

### Delmål 3: Collaborative Filtering (Uge 2)
**Status:** ⬜ Ikke startet

**Opgaver:**
- [ ] User-based collaborative filtering
- [ ] Item-based collaborative filtering
- [ ] Matrix Factorization (SVD eller ALS)
- [ ] Hyperparameter tuning
- [ ] Cross-validation for at undgå overfitting

**Færdig når:** Collaborative filtering model opnår RMSE < 1.0 på validation set.

---

### Delmål 4: Content-Based Filtering (Uge 3)
**Status:** ⬜ Ikke startet

**Opgaver:**
- [ ] Feature engineering fra movie metadata (genre, år, etc.)
- [ ] TF-IDF på film beskrivelser eller tags
- [ ] Cosine similarity mellem film
- [ ] Byg content-based recommender
- [ ] Evaluér performance

**Færdig når:** Content-based model kan give meningsfulde anbefalinger baseret på film features.

---

### Delmål 5: Hybrid System (Uge 3-4)
**Status:** ⬜ Ikke startet

**Opgaver:**
- [ ] Kombinér collaborative og content-based approaches
- [ ] Test forskellige weighted blending strategies
- [ ] Sammenlign performance: baseline vs CF vs content vs hybrid
- [ ] Håndter cold-start problem for nye brugere/film
- [ ] Final model selection

**Færdig når:** Hybrid model outperformer individuelle modeller og RMSE < 1.0 på test set.

---

### Delmål 6: Deployment & Interface (Uge 4)
**Status:** ⬜ Ikke startet

**Opgaver:**
- [ ] Gem trained model (pickle eller joblib)
- [ ] Byg simpel CLI eller web interface (Flask/Streamlit)
- [ ] User kan input user_id og få 10 anbefalinger
- [ ] Vis movie titles, genres, og predicted ratings
- [ ] Basic error handling

**Færdig når:** Prototype virker end-to-end og kan demonstreres.

---

### Delmål 7: Dokumentation & Rapportering (Uge 4-5)
**Status:** ⬜ Ikke startet

**Opgaver:**
- [ ] Skriv technical report i docs/
- [ ] Performance plots og sammenligninger
- [ ] Diskussion af findings og begrænsninger
- [ ] Næste skridt og potential improvements
- [ ] README opdatering med installation instructions
- [ ] Kod kommentarer og docstrings

**Færdig når:** Komplet dokumentation der forklarer metode, resultater, og hvordan man kører projektet.

---

## Overall Status
**Completion: 0/7 delmål færdige**

**Nuværende fase:** Ikke startet

**Næste handling:** Download MovieLens dataset og start EDA

---

## Teknisk Stack
- **Python 3.9+**
- **Libraries:** pandas, numpy, scikit-learn, surprise (for recommender algorithms)
- **Visualization:** matplotlib, seaborn
- **Optional:** scikit-surprise, LightFM, TensorFlow/PyTorch
- **Deployment:** Flask eller Streamlit

## Potentielle Udfordringer
- Cold-start problem (nye brugere uden ratings history)
- Sparse data matrix
- Computational cost for large datasets
- Balancing exploration vs exploitation

## Mulige Udvidelser
- A/B testing framework
- Real-time recommendations med streaming data
- Deep learning approaches (Neural Collaborative Filtering)
- Diversity og serendipity metrics
- Explainable recommendations