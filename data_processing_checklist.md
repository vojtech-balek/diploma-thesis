# Data Engineering and Preprocessing Checklist

This checklist is based on the "Item Properties" section described in the text. Use it to track progress on recreating the data engineering and preprocessing steps.

## 1. Properties Based on Content Data
These properties are based only on the content data and can be computed before the item is applied.

- [ ] **Complexity Measures**
  - [x] Text length
  - [ ] Text complexity (readability formulae, etc.)
  - [x] Domain-specific complexity (e.g., code complexity: number of lines, nesting depth, cyclomatic complexity)
- [x] **Item Form**
  - [x] Identify modalities of the stem and options (text, image, audio, code, math expressions, true/false, etc.)
- [ ] **Item Type**
  - [ ] Entailed cognitive processes (e.g., recalling, computing, constructing)
  - [ ] Map to Bloom's taxonomy (remember, understand, apply, analyze, evaluate, create)
  - [ ] Implement semi-automatic classification (e.g., using regular expressions over keywords)
- [ ] **Content Representation**
  - [ ] Bag-of-words representation
  - [ ] Vectors of TF-IDF weights
  - [ ] Automatic keyword identification (e.g., domain CEFR levels, used commands/keywords in code)

## 2. Properties Based on Performance Data
These properties are based on observed data about student performance across different items.

- [x] **Difficulty Measures**
  - [X] Error rate (proportion of students that made a mistake)
  - [X] Median response time
- [ ] **Item Discrimination**
  - [ ] Upper-lower discrimination index (difference in error rates between lower third and upper third of students)
  - [ ] Point-biserial index (correlation coefficient between overall error rate and the item answer)
- [ ] **Performance-based Item Similarity**
  - [ ] Calculate average similarity (Pearson correlation over responses for pairs of items)
- [ ] **Common Wrong Answers**
  - [ ] Analyze the distribution of specific wrong answers
  - [ ] Calculate numerical rates for the most common wrong answers to find specific flaws
