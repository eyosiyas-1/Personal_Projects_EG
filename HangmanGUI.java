import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.HashMap;
import java.util.Map;

public class HangmanGUI extends JFrame {
    private JLabel wordLabel;
    private JLabel hintLabel;
    private JLabel livesLabel;
    private JLabel levelLabel;
    private JTextField inputField;
    private JButton guessButton;
    private JButton hintButton;
    private JButton newGameButton;
    private Map<String, Integer> wordLevels;
    private int level;
    private String word;
    private StringBuilder guessedWord;
    private int hints;
    private int lives;

    public HangmanGUI() {
        setTitle("Hangman Game");
        setSize(400, 250);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new GridLayout(5, 1));

        wordLabel = new JLabel();
        hintLabel = new JLabel();
        livesLabel = new JLabel();
        levelLabel = new JLabel();
        inputField = new JTextField();
        guessButton = new JButton("Guess");
        hintButton = new JButton("Hint");
        newGameButton = new JButton("New Game");

        add(wordLabel);
        add(hintLabel);
        add(livesLabel);
        add(levelLabel);
        add(inputField);
        add(guessButton);
        add(hintButton);
        add(newGameButton);

        guessButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String guess = inputField.getText().toLowerCase();
                if (guess.length() != 1 || !Character.isLetter(guess.charAt(0))) {
                    JOptionPane.showMessageDialog(null, "Please enter a single letter.");
                    return;
                }

                if (!checkGuess(guess.charAt(0))) {
                    lives--;
                    livesLabel.setText("Lives: " + lives);
                    if (lives == 0) {
                        JOptionPane.showMessageDialog(null, "Game Over! The word was: " + word);
                        resetGame();
                    }
                }

                if (guessedWord.indexOf("_") == -1) {
                    JOptionPane.showMessageDialog(null, "Congratulations! You guessed the word: " + word);
                    level++;
                    resetGame();
                }

                inputField.setText("");
                wordLabel.setText("Word: " + guessedWord);
            }
        });

        hintButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                if (hints > 0) {
                    int index = guessedWord.indexOf("_");
                    guessedWord.setCharAt(index, word.charAt(index));
                    hints--;
                    hintLabel.setText("Hint: " + guessedWord);
                } else {
                    JOptionPane.showMessageDialog(null, "No more hints left!");
                }
            }
        });

        newGameButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                resetGame();
            }
        });

        initializeWordLevels();
        resetGame();
        setVisible(true);
    }

    private void initializeWordLevels() {
        wordLevels = new HashMap<>();
        wordLevels.put("puppy", 1);
        wordLevels.put("microwave", 2);
        wordLevels.put("witchcraft", 3);
        wordLevels.put("jawbreaker", 4);
        wordLevels.put("bandwagon", 5);
        wordLevels.put("zombie", 6);
        wordLevels.put("transcript", 7);
        wordLevels.put("gnarly", 8);
        wordLevels.put("pneumonia", 9);
        wordLevels.put("xylophone", 10);
    }

    private void resetGame() {
        word = getNextWord();
        guessedWord = new StringBuilder();
        for (int i = 0; i < word.length(); i++) {
            guessedWord.append("_");
        }
        wordLabel.setText("Word: " + guessedWord);
        hintLabel.setText("");
        hints = 3;
        lives = 6;
        livesLabel.setText("Lives: " + lives);
        levelLabel.setText("Level: " + wordLevels.get(word));
    }

    private String getNextWord() {
        for (String w : wordLevels.keySet()) {
            if (wordLevels.get(w) == level + 1) {
                return w;
            }
        }
        return "";
    }

    private boolean checkGuess(char guess) {
        boolean found = false;
        for (int i = 0; i < word.length(); i++) {
            if (word.charAt(i) == guess) {
                guessedWord.setCharAt(i, guess);
                found = true;
            }
        }
        return found;
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                new HangmanGUI();
            }
        });
    }
}
