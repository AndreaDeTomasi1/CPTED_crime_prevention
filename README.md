# 🏠 AI Risk Assessment for Insurance using CPTED

Questo progetto propone un sistema di intelligenza artificiale per la perizia assicurativa di immobili, basato sulla teoria CPTED (Crime Prevention Through Environmental Design) per la selezione delle feature rilevanti nella valutazione del rischio.

L’obiettivo è supportare gli assicuratori con uno strumento decisionale avanzato che integri dati strutturati dell’abitazione, informazioni territoriali e analisi di immagini satellitari per generare uno score di rischio della zona.

## 📌 Descrizione del Progetto

Il modello combina diverse fonti di dati:

Dati dell’immobile: metri quadri, presenza di sistemi di allarme e altre caratteristiche strutturali.

Feature stradali ottenute tramite OpenStreetMap.

Feature territoriali estratte da immagini satellitari di Google Maps, recuperate a partire dall’indirizzo dell’abitazione.

Analisi visiva tramite YOLOv8 per instance segmentation.

Tutte le feature vengono aggregate in un modello AdaBoost, che produce uno scoring del rischio facilmente consultabile attraverso un’interfaccia grafica dedicata agli assicuratori.

## ⚙️ Tecnologie Utilizzate

Python

AdaBoost (Machine Learning)

YOLOv8 (Instance Segmentation)

OpenStreetMap API

Google Maps Satellite Imagery

Roboflow (dataset labeling)

## 📂 Struttura del Repository
.
├── coding/
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

## 🔎 Pipeline del Sistema

Raccolta dati dell’immobile.

Estrazione delle feature territoriali tramite OpenStreetMap.

Download delle immagini satellitari basate sull’indirizzo.

Instance segmentation con YOLOv8.

Fusione delle feature in un modello AdaBoost.

Generazione dello score di rischio.

Visualizzazione tramite interfaccia grafica.

## 🚀 Possibili Applicazioni

Supporto alla valutazione del rischio assicurativo

Automazione delle perizie immobiliari

Analisi preventiva della sicurezza urbana

Decision support per underwriting

## 📚 Riferimenti

CPTED – Crime Prevention Through Environmental Design → vedi Paper_CPTED.pdf

Presentazione completa del progetto → Presentazione.pdf
