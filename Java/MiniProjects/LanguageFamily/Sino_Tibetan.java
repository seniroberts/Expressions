package LanguageFamily;

public class Sino_Tibetan extends Language {

    Sino_Tibetan(String name, int numSpeakers) {
        super(name, numSpeakers, "Asia", "subject-object-verb");
        if (name.contains("Chinese")) {
            this.wordOrder = "subject-verb-object";
        }

    }

    @Override
    public String getGreeting() {
        return "Ciao come stai oggi";

    }

}
