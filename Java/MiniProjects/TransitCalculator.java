
import java.util.Arrays;
import java.lang.Math;

public class TransitCalculator {
    int transitDays, numOfRides, age;
    boolean isDisabled;
    String location;

    String[] rideOptions = { "Pay-per-ride", "7-day-Unlimited", "30-day-Unlimited" };

    public TransitCalculator(int transitDays, int numOfRides, int age, boolean isDisabled, String location) {
        this.transitDays = transitDays;
        this.numOfRides = numOfRides;
        this.age = age;
        this.isDisabled = isDisabled;
        this.location = location;
    }

    public double[] getFares() {
        double[] faresByCity = new double[2];

        // Nyc Rates:
        double[] nycRatesRegular = { 2.75, 33.0, 127.0 };
        double[] nycRatesSubsidized = { 1.35, 16.50, 63.50 };

        // Paris Rates:
        double[] parisRatesRegular = { 3.23, 29.12, 110.00 };
        double[] parisRatesSubsidized = { 1.06, 9.50, 42.19 };

        // Logic to select fares based on location:

        if (location == "New York") {
            if (isDisabled = false || age < 65) {
                faresByCity = nycRatesRegular;
            } else {
                faresByCity = nycRatesSubsidized;
            }
        } else if (location == "Paris") {
            if (isDisabled = false || age < 65) {
                faresByCity = parisRatesRegular;
            } else {
                faresByCity = parisRatesSubsidized;
            }
        }

        return faresByCity;

    }

    public double unlimitedSevenPrice() {
        double[] faresByCity = getFares();
        double weeklyPrice = Math.ceil(transitDays / 7.0) * faresByCity[1];
        double finalPrice = weeklyPrice / numOfRides;
        return Math.round(finalPrice * 100.0) / 100.0;

    }
    // This method returns an array of price

    public double[] getRidePrices() {
        double[] faresByCity = getFares();
        double unlimitedThirty = faresByCity[2] / numOfRides;
        double unlimitedThirtyPrice = Math.round(unlimitedThirty * 100.0) / 100.0;
        double payPerRidePrice = numOfRides * faresByCity[0];
        double[] priceArray = { payPerRidePrice, unlimitedSevenPrice(), unlimitedThirtyPrice };
        return priceArray;
    }

    // Fare comparion method. It returns the lowest fare from the array of prices.
    public String getBestFare() {
        double[] priceList = getRidePrices();
        int lowestFareIndex = 0;
        for (int i = 0; i < getRidePrices().length; i++) {
            if (priceList[i] < priceList[lowestFareIndex]) {
                lowestFareIndex = i;

            }
        }
        return "Dear Customer, \n The cheapest fare option is the: " + rideOptions[lowestFareIndex] + " option at "
                + "$" + priceList[lowestFareIndex] + " per ride";
    }

    public static void main(String[] args) {
        TransitCalculator customer1 = new TransitCalculator(5, 12, 33, false, "New York");
        TransitCalculator customer2 = new TransitCalculator(26, 54, 43, true, "New York");
        TransitCalculator customer4 = new TransitCalculator(26, 54, 69, false, "Paris");
        TransitCalculator customer3 = new TransitCalculator(26, 54, 43, false, "Paris");

        System.out.println(customer1.getBestFare());
        System.out.println(customer2.getBestFare());
        System.out.println(customer3.getBestFare());
        System.out.println(customer4.getBestFare());

    }

}
