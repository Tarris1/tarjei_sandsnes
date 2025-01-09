# Pharmaceuticals (Unnamed Project): Simplifying pharmaceutical research

Analyzing pharmaceuticals is a highly time-consuming affair. My aim for this project was to combine all the tools that I would regularly use in my pharmaceuticals research in one large tool. By searching using a drug-id, you could get a list of pertinent research papers, chemistry data, patents, news articles, clinical trials, etc., all in one Excel file!

## Technology Stack / Methodology

This app is built entirely in **Python** and is terminal-based (i.e. it has no GUI). It functions thus as follows:
1. A .json database is established or loaded, where drugs that you have done research on can be stored.
2. The user can add new drugs to the database, edit the data stored on a particular drug, remove drugs, etc.
3. The user can search for drugs in their database. I.e. if you are researching mononuclear antibodies, you can easily look for all the ones you have looked at previously.
4. You can research a drug via @pubchem (chemistry data), @pubmed (research papers), @trials (clinicaltrials.gov), @news (newsapi.org), @patents (uspto.gov), or all of these via @report

## Addendums 

I have also, as part of this project, built a React-based version of the same app, which never went into fruition.

## Links
- [GitHub Repository Python](https://github.com/Tarris1/Pharmaceuticals)
- [GitHub Repository React](https://github.com/Tarris1/DrugsReact)