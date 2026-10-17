---
name: medical-procedure-reference
description: "Processador e consultor de tabelas de referência de procedimentos médicos (como TUSS e tabelas de operadoras de saúde). Use for: extrair informações sobre cobertura, autorização, documentação necessária e classificação de complexidade de procedimentos médicos, especialmente útil para hematologistas e especialistas em TMO consultarem regras de planos de saúde."
---

# Medical Procedure Reference

This skill enables Manus to efficiently process, query, and extract information from medical procedure reference tables (like TUSS and health insurance coverage tables).

## When to Use

Use this skill when the user asks to:
- Check if a specific medical procedure requires prior authorization
- Verify the required documentation for a procedure
- Determine the complexity level of an exam or procedure
- Cross-reference a procedure name with its code
- Analyze large PDFs or spreadsheets containing health insurance rules

## How to Use

### 1. Process Reference Documents
When given a reference document (PDF or Excel), use the bundled scripts to process it rather than trying to read the whole file into context.

```bash
# To search for a specific procedure in a PDF table
python scripts/search_procedure.py <pdf_path> "<search_term>"
```

### 2. Understand Coverage Rules
Medical procedure tables usually follow a standard structure. When interpreting the results, pay attention to:
- **DUT (Diretrizes de Utilização)**: Se um procedimento tem DUT, significa que ele só tem cobertura se o paciente se enquadrar em critérios clínicos específicos da ANS.
- **Autorização**: Se "SIM", o médico deve solicitar aprovação prévia da operadora antes de realizar o procedimento.
- **Alta Complexidade (PAC)**: Procedimentos marcados como PAC geralmente exigem justificativa médica detalhada.

### 3. Hematology / BMT Focus
When working with Hematology and Bone Marrow Transplant (TMO) procedures, specifically look for:
- Chemotherapy administration codes
- Stem cell collection and processing procedures
- Bone marrow aspiration and biopsy
- Flow cytometry and molecular tests (PCR)
- Transfusion procedures

## Best Practices

1. **Exact Matching**: Medical codes are exact. When searching by code, use exact matches.
2. **Fuzzy Searching**: When searching by name, use partial terms (e.g., "Mielograma" instead of "Punção aspirativa de medula óssea para mielograma") as nomenclature varies.
3. **Always Check Requirements**: Don't just say "it's covered". Always include if it needs authorization and what documentation is required.
