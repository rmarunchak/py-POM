import requests
import json


class GroupGenerator:

    @staticmethod
    def generate_group():
        # Credentials
        username = "admin"
        password = "Test123456"
        payload = {
            "group": {
                "parent_organization_id": 313,
                "group_nm": "auto_group_y4lv1qvicgk5xkth6cqal0qh9rb11kab",
                "registration_group_cd": "TG_g967pugst7xryuggrf6jai1gkfsx2561",
                "card_nm": "CD_kb36q85pjx",
                "group_type_cd": "GROUPTYPE_COMPANY",
                "lob_cdx": "LOBTYPE_MEDICAID",
                "lob_state": "CT",
                "fees": {
                    "primary_registration": {
                        "member": "0.00",
                        "company": "0.00"
                    },
                    "dependent_registration": {
                        "member": "0.00",
                        "company": "0.00"
                    }
                },
                "primary_source_cd": "REGTYPE_OPEN",
                "dependent_source_cd": "REGTYPE_OPEN",
                "standard_service_level_id": "2",
                "vip_service_level_id": "2",
                "permission_cancel_primary_flg": "N",
                "permission_cancel_dependents_flg": "N",
                "web_access_flg": "Y",
                "mobile_access_flg": "Y",
                "send_ccr_to_pcp_flg": "N",
                "send_card_flg": "N",
                "effective_start_dt": "05/02/2021",
                "consult_reimbursement_method_cd": "CONSULTREIMBURSEMENT_NA"
            }
        }
        response = requests.post("https://tas.redesign-master.qa.teladoc.io/v1/groups",
                                 json=payload,
                                 auth=(username, password))

        # Check the response status code
        if response.status_code == 200:
            try:
                result = response.json()
                return result
            except json.decoder.JSONDecodeError:
                print("Received an empty response or response not in JSON format.")
                return None
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return None


# Call the function
if __name__ == "__main__":
    result = GroupGenerator.generate_group()
    if result:
        print(result)
    else:
        print("Failed to generate group.")
