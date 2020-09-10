package LanguageFamily;

public class Language {

    protected String name;
    protected int numSpeakers;
    protected String regionsSpoken;
    protected String wordOrder;

    Language(String name, int numSpeakers, String regionsSpoken, String wordOrder) {
        this.name = name;
        this.numSpeakers = numSpeakers;
        this.regionsSpoken = regionsSpoken;
        this.wordOrder = wordOrder;

    }

    public void getInfo() {
        System.out.println(name + " is spoken by " + numSpeakers + " people mainly in " + regionsSpoken
                + ". The language follows the word order " + wordOrder);
    }

    public String getGreeting() {
        return "Hello, how are you today!";
    }

    public static void main(String[] args) {

        Antartican antica = new Antartican();
        antica.getInfo();
        System.out.println(antica.getGreeting());
        Language spanish = new Language("Spanish", 3000, "Europe", "Subject-Object-Verb");
        Manyan tzeltal = new Manyan("Tzeltal", 445856);
        Sino_Tibetan MandarinChinese = new Sino_Tibetan("Mandarin Chinese", 300000);
        Sino_Tibetan Brumese = new Sino_Tibetan("Burmese", 1500);
        System.out.println("****************************");
        spanish.getInfo();
        System.out.println("****************************");
        tzeltal.getInfo();
        System.out.println("****************************");
        MandarinChinese.getInfo();
        System.out.println("****************************");
        Brumese.getInfo();
    }

}
