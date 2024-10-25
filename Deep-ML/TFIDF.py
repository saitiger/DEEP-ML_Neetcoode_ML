import math 
def compute_tf_idf(corpus, query):
    """
    Compute Term Frequency for a term in a document.
    
    Args:
        document (list): List of words in the document
        term (str): Term to compute TF for
    
    Returns:
        float: Term frequency value
    """

    num_docs = len(corpus)
    results = []
    
    # Process each document
    for doc in corpus:
        doc_scores = []
        # Process each query term
        for term in query:
            # Calculate TF
            tf = doc.count(term) / len(doc) if len(doc) > 0 else 0
            
            # Calculate IDF with smoothing
            docs_with_term = sum(1 for d in corpus if term in d)
            idf = math.log((num_docs + 1)/(docs_with_term + 1)) + 1
            
            # Calculate TF-IDF
            tf_idf = round(tf * idf, 5)
            doc_scores.append(tf_idf)
            
        results.append(doc_scores)
    
    return results
  
# Without Built-in functions 
def compute_tf_idf(corpus, query):
    """
    Compute TF-IDF scores for a query against a corpus of documents.
    """
    num_docs = len(corpus)
    results = []
    
    # Iterating each document
    for doc in corpus:
        doc_scores = []
        # Iterating each query term
        for term in query:
            term_count = 0
            for word in doc:
                if word == term:
                    term_count += 1
            tf = term_count / len(doc) if len(doc) > 0 else 0
            
            # Calculate IDF with smoothing 
            docs_with_term = 0
            for d in corpus:
                # Check if term exists in document
                term_exists = False # Initialize as False 
                for word in d:
                    if word == term: 
                        term_exists = True # Break when term found
                        break
                if term_exists:
                    docs_with_term += 1
            
            idf = math.log((num_docs + 1)/(docs_with_term + 1)) + 1 # Smoothing to avoid division by Zero 
            tf_idf = round(tf * idf, 5)
            doc_scores.append(tf_idf)
        results.append(doc_scores)
    
    return results
