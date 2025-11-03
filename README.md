# Network_Useful_Function

A Python package that provides a collection of **useful network analysis, text analysis, and web scraping functions**.  
This package is designed to help you analyze graphs, compute community metrics, sample networks, process course descriptions, and scrape web content.

---

## Features

- **Graph utilities**
  - `all_shortest_from(G, node_i)`: Compute shortest path lengths from a node to all others in a graph.
  - `modularity(G, partition)`: Calculate modularity score for a community partition.
  - `snowball_sampling(G, seed_nodes, size, max_wave=2)`: Perform snowball sampling on a graph.
  - `snowball_sampling_shuffle(G, seed_nodes, size, max_wave=2)`: Snowball sampling with shuffled edge selection.

- **Text analysis**
  - `STOPWORDS`: Set of English stopwords loaded from `data/stopwords-en.txt`.
  - `get_word_frequencies_from_all_course_descriptions(course_descriptions)`: Count word frequencies in course descriptions excluding stopwords.

- **Web scraping**
  - `get_course_titles_and_descriptions(dept_html)`: Extract course titles and descriptions from a department HTML page.
  - `get_people_in_article(url)`: Extract linked people from a TMZ article.
  - `collect_people_from_random_articles(sample_size=10)`: Collect people from random articles (CSV-based).

---

## Installation

Make sure you are in the project root directory:

```bash
pip install -e .
