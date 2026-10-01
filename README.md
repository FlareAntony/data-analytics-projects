# Personal Python, SQL, & Data Automation Portfolio

A centralized repository showcasing production-grade automation scripts, high-precision financial calculators, data purification pipelines, and structured relational database assets engineered to eliminate operational risk and reduce business uncertainty.

## 📊 Project Index & System Architectures

### 1. Enterprise SQL Data Purification Script (`payroll_queries.sql`)
* **The Operational Problem:** Sifting through historical cross-border payroll entries containing corrupted text strings, missing inputs, and inconsistent regional formatting.
* **The Technical Solution:** Programmed a declarative SQL cleaning query leveraging explicit type-casting (`CAST AS REAL`) and logical database constraints (`WHERE`) to instantly isolate corrupted lines and quarantine extreme data-entry outliers. Implemented text standardization functions (`UPPER(REPLACE())`) to map irregular string data onto uniform corporate logging conventions on the fly.
* **Files:** Supported by `create_db.py` (database initialization) and `company_data.db` (the active sandbox ledger).

### 2. Deep Data Cleansing & Transaction Ingestion Engine (`data_cleaner.py`)
* **The Operational Problem:** Processing highly volatile human contractor logs packed with hidden whitespaces, missing rows, and multi-variable entry errors that threaten downstream corporate cash outflows.
* **The Technical Solution:** Built a resilient Python pipeline using robust string standardizations (`.strip()`, `.upper()`) and strict input type validation handlers (`None` checking). Engineered a statistical gatekeeper threshold to automatically flag and quarantine fat-finger calculation exceptions.

### 3. Multi-Variable Currency Arbitrage Calculator (`currency_arbitrage_v2.py`)
* **The Operational Problem:** Location-independent financial tracking models are historically rigid, breaking the moment cross-border expense ratios or individual budget strategies fluctuate.
* **The Technical Solution:** Architected an interactive financial utility handling multi-variable user inputs for discrete expense categories. Implemented an algorithmic percentage-based multiplier engine to seamlessly isolate liquid "Fun Money" buckets from a core, compounding S&P 500 capital accumulation pipeline.
