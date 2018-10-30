---
layout: default
---

## Current Summary of Project Progress

**Overview of project progress (10/30/2018 update)**

A condensed summary of work done so far

### _neisseria meningitidis_ 

* June / July 2018

1. Filter for wgMLST of carriage isolates
2. Extraction of data from BIGsdb using custom script (python)
3. Dataset cleanup
4. Allele frequency correlation analysis / plot (python)

### _streptococcus agalactiae_ (GBS)

* September / October 2018

Assembly Pipeline overview
  1. Download/Extract Data
    - PubMLST
    - ENA 
    - SRA
  2. Quality check with FASTQC and MultiQC
  3. Preprocessing with Trimmomatic using compiled database of adapters
  4. Quality check with FASTQC and MultiQC
  5. De novo assembly with SPADES
  6. Assembly quality check with Quast/ Visualization with Bandage
  7. Genome annotation with Prokka
  8. Pan-genome construction and core genome alignment with Roary
  9. Preliminary Data analyses with Roary output

```
Long, single-line code blocks should not wrap. They should horizontally scroll if they are too long. This line should be long enough to demonstrate this.
```

```
The final element.
```
