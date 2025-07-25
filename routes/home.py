from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from utils.s3_utils import list_weather_keys

router = APIRouter()

templates = Jinja2Templates(directory="templates")
router.mount("/static", StaticFiles(directory="static"), name="static")


AVAILABLE_CITIES = [
    "Delhi", "Mumbai", "Kolkata", "Chennai", "Bangalore",
    "Hyderabad", "Pune", "Ahmedabad", "Jaipur", "Lucknow",
    "Surat", "Kanpur", "Nagpur", "Indore", "Thane",
    "Bhopal", "Visakhapatnam", "Patna", "Vadodara", "Ghaziabad",
    "Ludhiana", "Agra", "Nashik", "Faridabad", "Meerut",
    "Rajkot", "Kalyan", "Vasai", "Varanasi", "Srinagar",
    "Aurangabad", "Dhanbad", "Amritsar", "Navi Mumbai", "Allahabad",
    "Howrah", "Gwalior", "Jabalpur", "Noida", "Jodhpur",
    "Coimbatore", "Vijayawada", "Madurai", "Raipur", "Kota",
    "Guwahati", "Chandigarh", "Solapur", "Hubli", "Mysore",
    "Bareilly", "Aligarh", "Moradabad", "Bhilai", "Tiruchirappalli",
    "Jamshedpur", "Bokaro", "Cuttack", "Ujjain", "Rourkela",
    "Bhavnagar", "Dehradun", "Asansol", "Nanded", "Kolhapur",
    "Ajmer", "Akola", "Gaya", "Siliguri", "Udaipur",
    "Thiruvananthapuram", "Thrissur", "Warangal", "Tirupati", "Panaji",
    "Imphal", "Shillong", "Aizawl", "Itanagar", "Gangtok"
]

@router.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("weather.html", {
        "request": request,
        "available_cities": AVAILABLE_CITIES,
        "all_keys": list_weather_keys()
    })