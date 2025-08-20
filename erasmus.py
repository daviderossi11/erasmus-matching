from dataclasses import dataclass
from typing import Optional, List

ALIMENTAZIONE = [
    "Vegetariana",
    "Vegana",
    "Omnivora",
    "Celiaca",
    "Intollerante al lattosio",
    "No carne di maiale",
    "No carne di manzo",
    "No pesce",
    "No crostacei",
    "No uova",
    "No frutta secca",
    "Altro",
] = Optional[str]

@dataclass
class Erasmus:
    """
    Represents an Erasmus program with its details.
    
    Attributes:
        id (int): Unique identifier for the Erasmus program.
        name (str): Name of the Erasmus program.
        description (str): Description of the Erasmus program.
        duration (int): Duration of the program in months.
        countries (List[str]): List of countries participating in the program.
        coordinator_email (Optional[str]): Email of the program coordinator, if available.
    """
    name: str
    email: str
    città: str
    lingue:: List[str]
    alimentazione: ALIMENTAZIONE

    def matchcittò(self, city: str) -> bool:
        """
        Check if the given city matches the program's city.
        
        Args:
            city (str): The city to match against the program's city.
        
        Returns:
            bool: True if the cities match, False otherwise.
        """
        return self.città.lower() == city.lower()
    
    def lingue_in_comune(self, languages: List[str]) -> int:
        """
        Returns the number of languages in common between the program's languages and the given list.

        Args:
            languages (List[str]): The list of languages to compare.

        Returns:
            int: Number of languages in common.
        """
        return len(set(lang.lower() for lang in languages) & set(l.lower() for l in self.lingue))