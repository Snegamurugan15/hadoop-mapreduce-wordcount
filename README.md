# Hadoop MapReduce Word Count

This is a Big Data fundamentals project focused on distributed text aggregation with Hadoop MapReduce. The repository now keeps the project in its natural format: Java MapReduce code, plus a small Python local simulator for quick validation before running on a Hadoop cluster.

## What The Project Does

The mapper tokenizes input text, removes common stop words, and emits `(word, 1)` pairs. The reducer aggregates counts per token. A combiner is configured to reduce network transfer between map and reduce phases.

## Repository Structure

- `java/WordCount.java` - Hadoop mapper, reducer, combiner, and job configuration.
- `java/StopWords.java` - stop-word helper used by the mapper.
- `src/wordcount.py` - local Python implementation of the same counting logic.
- `scripts/run_local_wordcount.py` - command-line test harness for local text input.

## Local Smoke Test

```powershell
python scripts/run_local_wordcount.py < sample.txt
```

## Hadoop Run Pattern

```bash
hadoop com.sun.tools.javac.Main java/WordCount.java java/StopWords.java
jar cf wordcount.jar *.class
hadoop jar wordcount.jar WordCount /input/text /output/wordcount
```

## Portfolio Note

This repo intentionally does not pretend to be a web dashboard. It is a code-first distributed processing project, which is the stronger format for MapReduce coursework.
