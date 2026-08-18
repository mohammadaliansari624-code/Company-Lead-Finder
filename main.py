import requests

#Apolo.io api key is used.
API = 'rCjEfQKkPwBKwDk3p_DA0g'
#Clearbit is used to get the domain of the company.
def company_domain(company_name):
    print(f"\n Your company name is {company_name}. Searching for domain...")
    try:
         url=f"https://autocomplete.clearbit.com/v1/companies/suggest?query={company_name}"
         Data=requests.get(url).json()

         if not Data:
              print(f"No domain found for {company_name}. Please check the company name and try again.")
              return

         domain = Data[0]['domain']
         print(f"Domain found: {domain}")

         #Apolo.io API is used to get the details of the company using the domain.
         apolo_url = f"https://api.apollo.io/v1/organizations/enrich?domain={domain}"
         headers = {"X-Api-Key": API}

         apolo_response = requests.get(apolo_url, headers=headers)

         if apolo_response.status_code == 200:
              org = apolo_response.json().get('organization', {})

#printing the details of the company.
              print(f"\nCompany Details for {company_name}:")
              print(f"Name: {org.get('name') or 'N/A'}")
              print(f"Website: {org.get('website_url') or 'N/A'}")
              print(f"LinkedIn: {org.get('linkedin_url') or 'N/A'}")
              print(f"location: {org.get('city') or 'N/A'}")
              print(f"Employees: {org.get('estimated_num_employees') or 'N/A'}")
              print(f"Description: {org.get('short_description') or 'N/A'}")
         else:
              print(f"Failed to retrieve company details from Apolo.io. Status code: {apolo_response.status_code}")
    except Exception as e:
         print(f"An error occurred: {e}")
# getting the company name from the user and calling the function to get the domain and details of the company.
if __name__ == "__main__":
     target = input("Enter the company name: ")
     company_domain(target)