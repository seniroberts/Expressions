package LanguageFamily;

public class Manyan extends Language {

    Manyan(String name, int numSpeakers) {
        super(name, numSpeakers, "Central America", "verb-object-subject");

    }

    @Override
    public void getInfo() {
        System.out.println(name + " is spoken by " + numSpeakers + " people mainly in " + regionsSpoken
                + ".The language follows the word order: " + wordOrder + ". Fun fact: " + name
                + " is an ergative language");

    }

    @Override
    public String getGreeting() {
        return "Hallo wie geht es dir heute";
    }

}
