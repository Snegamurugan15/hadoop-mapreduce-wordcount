import java.util.Set;

public class StopWords {
    private static final Set<String> WORDS = Set.of(
        "the", "and", "of", "to", "in", "a", "is", "for", "on", "with",
        "as", "by", "an", "be", "or", "from", "that", "this"
    );

    public static boolean contains(String token) {
        return WORDS.contains(token);
    }
}
