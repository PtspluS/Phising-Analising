from keras.models import Sequential, load_model
from keras.layers import Dense, Dropout
from keras.optimizers import Adam
import matplotlib.pyplot as plt


class Network:

    def __init__(self,  create = True):
        if not create :
            self.load()
        else :
            opt = Adam(learning_rate=0.001, beta_1=0.9, beta_2=0.999, amsgrad=False)
            imput_dim = 5
            self.model = Sequential()
            self.model.add(Dense(imput_dim, input_dim = imput_dim, kernel_initializer='random_normal', bias_initializer='ones', activation='relu'))
            self.model.add(Dense(imput_dim*4, kernel_initializer='random_normal', bias_initializer='ones', activation='relu'))
            self.model.add(Dropout(0.5))
            self.model.add(Dense(imput_dim*2, kernel_initializer='random_normal', bias_initializer='ones', activation='relu'))
            self.model.add(Dropout(0.5))
            self.model.add(Dense(imput_dim, kernel_initializer='random_normal', bias_initializer='ones', activation='relu'))
            self.model.add(Dropout(0.5))
            self.model.add(Dense(int(imput_dim/2), kernel_initializer='random_normal', bias_initializer='ones', activation='relu'))
            self.model.add(Dropout(0.5))
            self.model.add(Dense(1, kernel_initializer='random_normal', bias_initializer='ones', activation='sigmoid'))

            self.model.compile(loss='mean_squared_error', optimizer=opt, metric=['accuracy'])

        self.model.summary()

    def save(self):
        name = 'advanced_bot.h5'
        self.model.save(name)
        print("The model is saved as : " + name)

    def load(self):
        self.model = load_model('advanced_bot.h5')
        print('Model loaded from : advanced_bot.h5')

    def predict(self, mail_params):
        out = self.model.predict(mail_params)
        return out

    def train(self, training_data, target_data, epochs = 1000, batch_size = 1, verbose = 0):
        history = self.model.fit(training_data, target_data, epochs= epochs, batch_size= batch_size, verbose=verbose)

        scores = self.model.evaluate(training_data, target_data, verbose=1)
        print('Test loss:', scores[0])
        print('Test accuracy:', scores[1])
        plt.plot(history.history['loss'])
        plt.plot(history.history['accuracy'])
        plt.show()