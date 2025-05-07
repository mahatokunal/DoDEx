# DoDEx

**Winner of the People’s Choice Award | Bitcamp Hackathon, University of Maryland (April 2024)**  
**[View on Devpost](https://devpost.com/software/ai-powered-extractor-for-defense-contract)**  

DoDEx (Defense Contract Data Extractor) is an AI-powered solution designed to streamline the process of parsing, extracting, and validating critical information from Defense Contract Notices.

## Inspiration

This project addresses the need for efficiency and accuracy in handling Defense Contract information. Traditional methods are often manual and error-prone. With AI tools and technologies, DoDEx was created to address these challenges.

## What It Does

DoDEx is an intelligent parser that automatically extracts key attributes from Defense Contract Notices. It captures and validates key information such as:
- Federal Agency
- Contract Amounts
- Important Dates
- Company Names
- Locations  
- And more...

The system validates the extracted data and provides an accuracy score, ensuring reliability.

## Key Features

- **AI-Driven Parser**  
  - Built using **C#** and **Angular**, enhanced with **Large Language Models (LLM)** and **Retrieval-Augmented Generation (RAG)**.
  - Achieved a **30% improvement** in validation accuracy for Defense Contract Notices.

- **Web Scraping and Validation Pipeline**  
  - Developed in **C#**, this pipeline extracts and categorizes key contract data.
  - Ensures high accuracy through advanced AI-driven validation techniques.

## How We Built It

1. **Web Scraping**  
   Scraped the Defense Contracts website to gather raw data using web scraping tools.

2. **AI-Driven Parsing**  
   Leveraged **LLM** to analyze the scraped data and extract relevant attributes like Federal Agency names, contract amounts, dates, and company names.

3. **Validation**  
   Applied **Retrieval-Augmented Generation (RAG)** to validate the extracted data, ensuring its accuracy and reliability.

4. **Technological Stack**  
   - **Languages**: Python (primary), C#  
   - **Frameworks**: Angular  
   - **AI Models**: LLM, RAG  
   - **Tools**: Web scraping libraries, validation algorithms

## Challenges We Faced

- Crafting effective prompts for the LLM to ensure accurate data extraction.  
- Validating the generative data to build trust in the AI-driven output.  
- Addressing the paradox of validation: "How is my LLM generating correct data? Because my LLM says so!"  

Through rigorous testing and iteration, we overcame these challenges by integrating **RAG** as a validation mechanism.

## Accomplishments We're Proud Of

- Successfully developed a highly effective AI-powered solution within a limited timeframe.  
- Streamlined the process of extracting and categorizing Defense Contract data.  
- Enhanced the accuracy and reliability of the extracted information through advanced validation techniques.  

## What We Learned

- The importance of robust validation mechanisms in critical domains like defense.  
- Techniques for handling large volumes of heterogeneous data efficiently.  
- How to integrate cutting-edge AI technologies (LLM and RAG) into real-world applications.  

## What's Next for DoDEx

- **Refining Prompts**: Enhance the LLM prompts to further improve accuracy.  
- **Expanding to New Domains**: Extend the solution to other fields like law, education, and healthcare.  
- **Scaling the System**: Build a more scalable version to handle larger datasets and more complex use cases.  

## Installation and Setup

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/mahatokunal/DoDEx.git
   cd DoDEx
   ```

2. **Install Dependencies**  
   Ensure Python is installed. Then, install the required packages:  
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**  
   ```bash
   python main.py
   ```

## Contribution Guidelines

We welcome contributions to improve DoDEx!  

1. Fork the repository.  
2. Create a new branch for your feature or bug fix.  
3. Commit your changes and open a pull request.  

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For questions, feedback, or contributions, please reach out:  

- **Owner**: [Kunal Mahato](https://github.com/mahatokunal)  , [Nidhi Kamath](https://github.com/nidhikamath2102) , [Manim Tirkey](https://github.com/manimtirkey2000)
- **Devpost**: [DoDEx on Devpost](https://devpost.com/software/ai-powered-extractor-for-defense-contract)
- **LinkedIn**: [Problem Statement by Bloomberg Industry Group](https://www.linkedin.com/posts/subashjohn_bloombergindustrygroup-bitcamp-umd-activity-7188114085329219585-T9uz/)

## Contributors

- **Kunal Mahato** ([mahatokunal](https://github.com/mahatokunal))  
- **Nidhi Kamath** ([nidhikamath2102](https://github.com/nidhikamath2102))  
- **Manim Tirkey** ([manimtirkey2000](https://github.com/manimtirkey2000))
