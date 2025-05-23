# Electronic-health-record-embedding

Overview
This project explores the use of transformer-based models—specifically BERT—for embedding Electronic Health Records (EHR) to predict short-term hospitalization risk in elderly patients. By leveraging advanced pre-training and fine-tuning strategies, the project demonstrates how deep learning can uncover meaningful patterns in complex healthcare data and improve predictive modeling for patient outcomes.

Key Features
BERT for EHR Data:
Adapts the BERT architecture to process sequences of diagnoses and hospital events, treating each diagnosis code as a word and each hospitalization as a sentence for effective embedding.

Pre-training Strategies:
Experiments with Masked Language Modeling (MLM) and Next Sentence Prediction (NSP) tasks, as well as their combination, to pre-train BERT on synthetic EHR data.

Custom Downstream Task:
Fine-tunes the model to predict whether a patient's clinical history will lead to a hospitalization event within three months, using a custom classification task tailored to healthcare trajectories.

Performance Evaluation:
Compares non-pretrained, pretrained, and further-pretrained BERT models, showing that domain-specific pre-training significantly boosts performance on the target prediction task (best accuracy: ~87%, best F1: ~91%).

Synthetic Dataset:
Uses a synthetic dataset of 680 elderly patients, each with multiple hospitalizations and up to five diagnoses per event, ensuring privacy and ethical compliance.

Project Structure
text
├── data/
│   └── (synthetic EHR data and preprocessing scripts)
├── src/
│   ├── bert_pretrain.py
│   ├── bert_finetune.py
│   └── utils.py
├── requirements.txt
├── train.py
├── evaluate.py
└── README.md
Getting Started
Clone the repository

bash
git clone https://github.com/edoppiap/bert_medical_records.git
cd bert_medical_records
Install dependencies

bash
pip install -r requirements.txt
Prepare data

Use the provided synthetic EHR dataset or adapt your own data following the described structure.

Pre-train BERT on EHR data

bash
python src/bert_pretrain.py --task mlm_nsp --epochs 8
Fine-tune on the downstream classification task

bash
python src/bert_finetune.py --epochs 1
Evaluate the model

bash
python evaluate.py
Results
Domain-adapted BERT models significantly outperform generic pretrained models for EHR-based risk prediction.

The best results were obtained by further pre-training BERT on EHR data using MLM and NSP tasks, followed by fine-tuning on the custom classification task.

Citation
If you use this work, please cite:

text
@misc{pietropaolo2024ehr,
  title={Applied Data Science Project: EHR embedding},
  author={Emanuele Pietropaolo and Yuting Wang and Rahul Kumar Sahoo},
  year={2024},
  howpublished={\url{https://github.com/edoppiap/bert_medical_records}}
}
Acknowledgments
Project by Emanuele Pietropaolo, Yuting Wang, and Rahul Kumar Sahoo, Politecnico di Torino.
