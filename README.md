# 🏠 AI Risk Assessment for Insurance using CPTED

Questo progetto propone un sistema di **intelligenza artificiale per la perizia assicurativa di immobili**, basato sulla teoria **CPTED (Crime Prevention Through Environmental Design)** per la selezione delle feature rilevanti nella valutazione del rischio.

L’obiettivo è supportare gli assicuratori con uno **strumento decisionale avanzato** che integri dati strutturati dell’abitazione, informazioni territoriali e analisi di immagini satellitari per generare uno **score di rischio della zona**.

---

## 📌 Descrizione del Progetto

Il modello combina diverse fonti di dati:

- **Dati dell’immobile**: metri quadri, presenza di sistemi di allarme e altre caratteristiche strutturali.

- **Feature stradali** ottenute tramite **OpenStreetMap**.

- **Feature territoriali** estratte da immagini satellitari di **Google Maps**, recuperate a partire dall’indirizzo dell’abitazione.

- **Analisi visiva** tramite **YOLOv8** per instance segmentation.

Tutte le feature vengono aggregate in un modello **AdaBoost**, che produce uno **scoring del rischio** facilmente consultabile attraverso **un’interfaccia grafica dedicata agli assicuratori**.

## ⚙️ Tecnologie Utilizzate

- Python

- AdaBoost (Machine Learning)

- YOLOv8 (Instance Segmentation)

- OpenStreetMap API

- Google Maps Satellite API

- Roboflow (dataset labeling)

## 📂 Struttura del Repository

```

.
├── coding/
|   ├──APP/
|   |  └── Codice per applicazione Streamlit
│   ├── Codici utilizzati per preprocessing, feature extraction e training
│   └── Modello YOLOv8
│
├── dataset/
│   ├── CSV delle abitazioni e dei sinistri forniti
│   └── Dataset etichettato con Roboflow per YOLOv8 (instance segmentation)
│
├── output/
│   └── File CSV generati dai vari script
│
├── output_satellite_maps/
│   └── Immagini satellitari da Google Maps
│
├── output_satellite_maps_zoom/
│   └── Immagini satellitari con zoom maggiore
│
├── Paper_CPTED.pdf        # Paper sulla teoria CPTED
└── Presentazione.pdf      # Presentazione del progetto

```

## 🔎 Pipeline del Sistema

1. Raccolta dati dell’immobile.

2. Estrazione delle feature territoriali tramite OpenStreetMap.

3. Download delle immagini satellitari basate sull’indirizzo.

4. Instance segmentation con YOLOv8.

5. Fusione delle feature in un modello AdaBoost.

6. Generazione dello score di rischio.

7. Visualizzazione tramite interfaccia grafica.

## 🚀 Possibili Applicazioni

- Supporto alla valutazione del rischio assicurativo

- Automazione delle perizie immobiliari

- Analisi preventiva della sicurezza urbana

- Decision support per underwriting

## 📚 Riferimenti

- **CPTED – Crime Prevention Through Environmental Design** → vedi `Paper_CPTED.pdf`

- Presentazione completa del progetto → `Presentazione.pdf`

## ⚠️ Note sul Repository

Per via dei limiti di dimensione imposti da GitHub, non è stato possibile caricare l’intero set di dati utilizzato durante lo sviluppo del progetto. Alcuni file, in particolare quelli relativi alle immagini satellitari e ai dataset completi, sono stati quindi esclusi dal repository.

Questo progetto ha principalmente **finalità dimostrative e accademiche**. Di conseguenza, i codici presenti potrebbero non essere completamente integrati tra loro o pronti per un utilizzo in produzione. L’obiettivo è mostrare l’approccio metodologico, le tecniche impiegate e il funzionamento generale della pipeline.
