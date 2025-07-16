import pandas as pd
from fuzzywuzzy import fuzz

class MedicineValidator:
    def __init__(self, reference_path):
        self.reference_db = pd.read_csv(reference_path)
    
    def validate_name(self, name):
        """Check medicine name against reference"""
        if not name:
            return False
        best_match = max(
            [(ref_name, fuzz.ratio(name.lower(), ref_name.lower())) 
             for ref_name in self.reference_db['name']],
            key=lambda x: x[1]
        )
        return best_match[1] > 80  # Threshold for valid match
    
    def validate_fields(self, info_dict):
        """Check all critical fields"""
        errors = []
        if not self.validate_name(info_dict["medicine_name"]):
            errors.append("Invalid medicine name")
        if not info_dict["batch_no"]:
            errors.append("Missing batch number")
        if not info_dict["expiry_date"]:
            errors.append("Missing expiry date")
        return errors