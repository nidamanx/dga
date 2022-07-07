# DGA
## Domain Generation Algorithms

### Disclaimer
**Do not attempt to use these tools to violate the law. The author is not responsible for any illegal action. Misuse of the provided information can result in criminal charges.**

### Description

Domain generation algorithms (DGA) are algorithms seen in various families of malware that are used to periodically generate a large number of domain names that can be used as rendezvous points with their command and control servers. The large number of potential rendezvous points makes it difficult for law enforcement to effectively shut down botnets, since infected computers will attempt to contact some of these domain names every day to receive updates or commands. The use of public-key cryptography in malware code makes it unfeasible for law enforcement and other actors to mimic commands from the malware controllers as some worms will automatically reject any updates not signed by the malware controllers.

For example, an infected computer could create thousands of domain names and would attempt to contact a portion of these with the purpose of receiving an update or commands.

Embedding the DGA instead of a list of previously-generated (by the command and control servers) domains in the unobfuscated binary of the malware protects against a strings dump that could be fed into a network blacklisting appliance preemptively to attempt to restrict outbound communication from infected hosts within an enterprise.

The technique was popularized by the family of worms Conficker.a and .b which, at first generated 250 domain names per day. Starting with Conficker.C, the malware would generate 50,000 domain names every day of which it would attempt to contact 500, giving an infected machine a 1% possibility of being updated every day if the malware controllers registered only one domain per day. To prevent infected computers from updating their malware, law enforcement would have needed to pre-register 50,000 new domain names every day. From the point of view of botnet owner, they only have to register one or a few domains out of the several domains that each bot would query every day.

Recently, the technique has been adopted by other malware authors. According to network security firm Damballa, the top-5 most prevalent DGA-based crimeware families are Conficker, Murofet, BankPatch, Bonnana and Bobax as of 2011.

DGA can also combine words from a dictionary to generate domains. These dictionaries can be hard-coded in malware or taken from a publicly accessible source. Domains generated by dictionary DGA tend to be more difficult to detect due to their similarity to legitimate domains. 
  
### Detection

DGA domain names can be blocked using blacklists, but the coverage of these blacklists is either poor (public blacklists) or wildly inconsistent (commercial vendor blacklists). Detection techniques belong in two main classes: reactionary and real-time. Reactionary detection relies on non-supervised clustering techniques and contextual information like network NXDOMAIN responses, WHOIS information, and passive DNS to make an assessment of domain name legitimacy. Recent attempts at detecting DGA domain names with deep learning techniques have been extremely successful, with F1 scores of over 99%. These deep learning methods typically utilize LSTM and CNN architectures, though deep word embeddings have shown great promise for detecting dictionary DGA. However, these deep learning approaches can be vulnerable to adversarial techniques.

---

#### Source
https://en.wikipedia.org/wiki/Domain_generation_algorithm
