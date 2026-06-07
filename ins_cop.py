from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

def askllm(user_prompt, system_prompt=" "):

    stream = client.chat.completions.create(
        model = 'gpt-4o-mini',
        messages = [
            {
                "role":"system",
                "content":system_prompt
            },
            {
                "role":"user",
                "content":user_prompt
            }
],
        temperature = 0.1,
        stream=True
    )
    
    
    print(stream)
    return stream

PRODUCTS = {
  "term_life_insurance": {
    "name": "Term Life Insurance",
    "coverage": "₹25L - ₹1Cr",
    "tenure": "10 - 40 years",
    "approximate_premium": "₹200 - ₹500/month (age 30, ₹50L cover, 20 years)",
    "sum_assured": "₹25L - ₹1Cr",
    "features": [
      "Affordable premiums",
      "High coverage amount",
      "Flexible payment options",
      "Additional riders (critical illness, accidental death)",
      "Online instant approval"
    ],
    "benefits": "Tax deductible under Section 80C (premium) and 10(10D) (maturity)"
  },
  "health_insurance": {
    "name": "Comprehensive Health Insurance",
    "coverage": "₹5L - ₹1Cr",
    "min_age": "18 years",
    "max_age": "65 years",
    "approximate_premium": "₹250 - ₹800/month (family, ₹5L coverage)",
    "sum_assured": "₹5L - ₹1Cr",
    "features": [
      "Cashless hospitalization at 8000+ hospitals",
      "No waiting period for accidental injuries",
      "Pre-hospitalization & post-hospitalization coverage (30 days)",
      "Family floater options",
      "Maternity and newborn coverage",
      "Dental and vision benefits"
    ],
    "benefits": "Premium eligible for tax deduction under Section 80D, annual health checkups"
  },
  "motor_insurance": {
    "name": "Car Insurance",
    "types": {
      "third_party": "Covers liability to third parties (mandatory), approx ₹2,000-5,000/year",
      "comprehensive": "Covers own vehicle damage + third party liability, approx ₹3,000-8,000/year"
    },
    "approximate_premium": "₹2,000 - ₹8,000/year (depends on vehicle value and type)",
    "sum_assured": "As per vehicle value",
    "features": [
      "24/7 roadside assistance",
      "Cashless claim settlement at 1000+ garages",
      "Zero depreciation cover for first 5 years",
      "Accidental damage coverage",
      "Personal accident cover (₹1L - ₹5L)"
    ],
    "benefits": "Mandatory by Indian Motor Vehicles Act"
  },
  "home_insurance": {
    "name": "Home/Property Insurance",
    "coverage": "Building + Contents",
    "approximate_premium": "₹3,000 - ₹10,000/year (₹50L building value)",
    "sum_assured": "Building replacement cost + contents coverage",
    "features": [
      "Coverage against fire, theft, natural disasters",
      "Reinstatement value coverage (replacement without depreciation)",
      "Replacement of contents and fixtures",
      "Cashless claim settlement",
      "All-risk personal belongings coverage",
      "Electrical & electronics coverage"
    ],
    "benefits": "Premium deductible under Section 80C, optional return of premium riders"
  },
  "travel_insurance": {
    "name": "Travel Insurance",
    "coverage": "Domestic & International",
    "approximate_premium": "₹500 - ₹3,000 (single trip), ₹2,000 - ₹10,000 (annual)",
    "sum_assured": "Medical: ₹5L - ₹50L, Trip cost protection: ₹5L - ₹20L",
    "features": [
      "Medical emergency coverage (24/7 assistance)",
      "Flight delay/cancellation benefits (₹100/hour after 6 hours)",
      "Baggage loss/delay protection",
      "Personal accident cover",
      "Trip cancellation protection",
      "Lost passport & visa assistance"
    ],
    "benefits": "Affordable peace of mind for domestic and international travels"
  },
  "critical_illness_insurance": {
    "name": "Critical Illness Insurance",
    "coverage": "₹10L - ₹1Cr",
    "approximate_premium": "₹400 - ₹1,200/month (age 30, ₹25L cover)",
    "sum_assured": "₹10L - ₹1Cr",
    "illnesses_covered": "40+ critical illnesses including cancer, heart attack, stroke, kidney failure, organ transplant",
    "features": [
      "Lump sum payout upon diagnosis (no deduction)",
      "Lifetime coverage option available",
      "Early detection benefit rider (50% of sum assured)",
      "Waiver of premium on claim",
      "Optional return of premium rider",
      "Multiple occurrence coverage (up to 3 claims)"
    ],
    "benefits": "Financially secure during recovery, covers treatment costs"
  },
  "endowment_plans": {
    "name": "Endowment Insurance Plans",
    "tenure": "10 - 20 years",
    "approximate_premium": "₹5,000 - ₹20,000/month (₹25L sum assured)",
    "sum_assured": "₹10L - ₹1Cr",
    "guaranteed_returns": "8-10% per annum (approximate)",
    "features": [
      "Guaranteed maturity benefit",
      "Regular bonuses (annual/loyalty bonus)",
      "Life cover during policy tenure (1-2x premium)",
      "Flexible withdrawal options after 3 years",
      "Policy loan facility (up to 80% of surrender value)"
    ],
    "benefits": "Combination of protection and savings with guaranteed returns, tax benefits"
  },
  "child_education_plans": {
    "name": "Child Education Insurance",
    "coverage": "Educational expenses for child",
    "approximate_premium": "₹3,000 - ₹10,000/month (₹20L maturity benefit)",
    "sum_assured": "₹20L - ₹1Cr at maturity",
    "features": [
      "Guaranteed education funding at maturity",
      "Parental death benefit (full premium waived)",
      "Annual bonuses",
      "Partial withdrawal for college fees (after 5 years)"
    ],
    "benefits": "Secure education funding for child, tax benefits under 80C"
  },
  "personal_accident_insurance": {
    "name": "Personal Accident Insurance",
    "coverage": "Accidental death & disability",
    "approximate_premium": "₹300 - ₹1,000/year (₹10L cover)",
    "sum_assured": "₹5L - ₹50L",
    "features": [
      "Accidental death benefit (full sum assured)",
      "Permanent total disability benefit",
      "Temporary disability benefit (₹100/day for 365 days max)",
      "Hospitalization expenses reimbursement",
      "Medical treatment coverage"
    ],
    "benefits": "Comprehensive accident coverage with high claim ratio"
  }
}

SYSTEM_PROMPT = f"""
You are a banking bot from Secure Bank.

Answer the questions of users in a polite and considerate manner.
Always greet the user before giving an answer.
Always address the user's question first and then give answers.
Users can use 'FD' as a short form of Fixed Deposit.
You only answer questions related to:
- Savings Account
- Fixed Deposit (FD)
- Car Loan
- Home Loan

Available products:
{PRODUCTS}

For any other question outside these products, respond exactly:
'Please ask questions about Secure Bank products only.'
"""
    
#askllm("does secure bank offers savings account",SYSTEM_PROMPT) 