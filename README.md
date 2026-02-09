Abstract

This project implements an on-premise, retrieval-augmented decision support system designed for Maharashtra Government / BMC–style administrative use cases. The system ingests statutory Acts and Rules (JSON) along with reference and contextual documents (PDFs), converts them into structured semantic embeddings, and enables controlled, auditable, and conservative policy interpretation.

The system does not approve, reject, or recommend actions. Instead, it assists officers by retrieving relevant legal provisions and clearly separating:
what can be concluded,
what cannot be concluded, and
what requires further confirmation,
thereby supporting defensible decision-making under policy ambiguity.

Key outcomes achieved:
Large-scale ingestion of statutory and contextual documents
Authority-aware metadata tagging (statutory vs contextual)
Persistent vector database for fast semantic retrieval
Conservative RAG responses with explicit limitations
Modular, production-ready code structure suitable for team testing

Project Structure:-
policy-rag/
├─ app/
│  ├─ ingest/
│  ├─ retrieval/
│  ├─ rag/
│  ├─ llm/
│  └─ config/
│
├─ data/                 # RAW DATA ONLY (gitignored)
│  ├─ json_files/        # Statutory Acts / Rules
│  └─ pdf_files/         # Reference / contextual PDFs
│
├─ notebooks/            # Optional experiments only
│  └─ Data/
│     └─ vector_store/   # Vector DB (gitignored, on-prem)
│
├─ main.py
├─ README.md
├─ requirements.txt
└─ .gitignore


🔧 Prerequisites
Python 3.9+
Virtual environment support
Ollama installed locally
No cloud or enterprise LLM API keys required

LLM Inference
Runtime: Ollama (fully on-prem)
Default model: llama3.1:latest
Inference characteristics:
Deterministic (low temperature)
No outbound network calls
Suitable for audit-constrained environments

🚀 Setup Instructions
1️⃣ Clone the Repository
git clone https://github.com/ayushvakani/policy-rag
cd policy-rag
2️⃣ Create and Activate Virtual Environment
python -m venv .venv
.venv\Scripts\activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Install Ollama and Pull Model
ollama pull llama3.1:latest
5️⃣ Configure Environment Variables
Create a .env file at the project root (optional overrides only):
VECTOR_DB_PATH=notebooks/Data/vector_store
 Add Data
data/
├── pdf_files/     # PDFs (manuals, reports, reference docs)
└── json_files/    # Acts, rules, circulars (structured JSON)

📥 One-Time Ingestion Step
⚠️ This step can take significant time depending on data size.
python -m app.ingest.ingest_documents

▶️ Running the System
After ingestion is complete:
python main.py

You should see:
System ready.
Documents: <count>
Enter query (or 'exit'):

🔍 Example Queries

What penalties are prescribed under the Act 1967?
Are contractual sanitation workers eligible for welfare benefits?
Does non-segregation of waste attract penalties under municipal rules?
Which provisions govern solid waste management responsibilities?



