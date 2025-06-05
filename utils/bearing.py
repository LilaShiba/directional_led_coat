import math

def calculate_bearing(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """
    Calculate the initial bearing (forward azimuth) from point A to point B.

    Args:
        lat1, lon1: Latitude and Longitude of the current location (degrees)
        lat2, lon2: Latitude and Longitude of the destination (degrees)

    Returns:
        Bearing in degrees (0° = North, 90° = East, etc.)
    """
    # Convert latitude and longitude from degrees to radians
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    # Difference in the longitudes
    dLon = lon2_rad - lon1_rad
    """ 
    sin(θ)	oppositehypotenusehypotenuseopposite​	Height or vertical part
    cos(θ)	adjacenthypotenusehypotenuseadjacent​	Width or horizontal part
    tan(θ)	oppositeadjacentadjacentopposite​	Vertical/horizontal slope
    """
    # Compute the bearing
    y = math.sin(dLon) * math.cos(lat2_rad)
    x = math.cos(lat1_rad) * math.sin(lat2_rad) - \
        math.sin(lat1_rad) * math.cos(lat2_rad) * math.cos(dLon)

    bearing_rad = math.atan2(y, x)

    # Convert to degrees and normalize to 0–360°
    bearing_deg = (math.degrees(bearing_rad) + 360) % 360

    return bearing_deg
