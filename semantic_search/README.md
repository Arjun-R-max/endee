# Enterprise Semantic Search System Using Endee Vector Database

![AI-Powered](https://img.shields.io/badge/AI-Semantic--Search-blueviolet)
![Vector DB](https://img.shields.io/badge/Database-Endee-green)
![Python](https://img.shields.io/badge/Language-Python-blue)

## 📌 Project Overview
This project implements an industry-grade **Semantic Search System** leveraging **Endee** as the core vector database. Unlike traditional keyword matching, this system understands the intent and contextual meaning behind queries, enabling precise retrieval from unstructured textual data.

Built within a fork of the official Endee repository, this project serves as a foundational retrieval layer for RAG (Retrieval-Augmented Generation) and recommendation engines.

---

## 🎯 Objectives
* **Vector Integration:** Demonstrate practical usage of dense vector embeddings in a production-like environment.
* **Endee Mastery:** Utilize Endee for efficient high-dimensional vector storage and similarity querying.
* **Scalable Architecture:** Provide a modular codebase that can be extended into full-scale RAG pipelines.

---

## ✅ Evaluation Criteria Mapping
| Requirement | Status |
| :--- | :--- |
| **Fork the Endee Repository** | ✅ Completed |
| **Use Endee as Vector Database** | ✅ Used for storage & search |
| **Practical AI/ML Use Case** | ✅ Semantic Search |
| **Vector-based Similarity Search** | ✅ Embeddings + Cosine Similarity |
| **Clean & Modular Structure** | ✅ Organized scripts & documentation |

---

## 🧠 System Architecture



1.  **Data Source:** Raw text documents (e.g., HR policies) are stored in `documents.txt`.
2.  **Embedding Generation:** Uses `SentenceTransformer` to convert text into $n$-dimensional dense vectors.
3.  **Vector Storage:** Embeddings and metadata are indexed within the **Endee** database.
4.  **Semantic Search:**
    * The user query is embedded into the same vector space.
    * Endee performs a similarity search (Cosine Similarity).
    * The system returns the most contextually relevant documents.

---

## 📂 Project Structure
```text
semantic_search/
│
├── data/
│   └── documents.txt         # Raw text dataset (one doc per line)
│
├── scripts/
│   ├── ingest_data.py        # Generates embeddings & populates Endee
│   ├── semantic_search.py    # Logic for similarity search queries
│   └── __init__.py
│
├── main.py                   # User-friendly CLI entry point
└── README.md                 # Project documentation

```

## 🚀 How to Run the Project

### 1️⃣ Clone Your Forked Repository

```bash
git clone https://github.com/<your-username>/endee.git
cd endee
```

### 2️⃣ Create Virtual Environment & Install Dependencies

```bash
python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt
pip install sentence-transformers
```

### 3️⃣ Add Sample Data

Edit the file:
```bash
semantic_search/data/documents.txt
```

Add one document per line.

###  4️⃣ Ingest Data into Endee

```bash
python semantic_search/scripts/ingest_data.py
```

This step:
-Converts documents into embeddings
-Stores them inside Endee vector database

### 5️⃣ Run Semantic Search Application

```bash
python semantic_search/scripts/semantic_search.py
python semantic_search/main.py
```

## 🧪 Sample Output
Query:
```vbnet
what is working hours from monday to friday?
```

Result:
```vbnet
Top Results:
1. (0.83) Working hours are from 9:30 AM to 6:30 PM, Monday to Friday.
2. (0.45) The organization follows a hybrid work model.
3. (0.34) Employees are entitled to annual leave.
```

## 🔍 Why Semantic Search?

Unlike keyword-based search, semantic search:
* Understands meaning and context
* Handles synonyms and paraphrased queries
* Forms the retrieval backbone of RAG systems

This project focuses on the retrieval layer, which is the most critical component of modern AI applications.

## 🧩 Extensibility

This system can be extended to:
* Retrieval-Augmented Generation (RAG)
* AI chatbots over documents
* Recommendation systems
* Agentic AI workflows

## 🏁 Conclusion

This project demonstrates a real-world AI/ML application using Endee as the vector database, satisfying all evaluation criteria.
It showcases core concepts required in industry-grade AI systems such as embeddings, vector storage, and semantic similarity search.

## 🔗 References

Endee Vector Database: https://github.com/EndeeLabs/endee
