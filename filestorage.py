class CarsList:

    def read_makes(self):
        """Reads a file with car makes and returns a list with no line breaks."""

        with open("car_makes.txt", "r") as makes:
            make_list = makes.readlines()
            for i, make in enumerate(make_list):
                make_list[i] = make.strip()
            return make_list

    def read_models(self):
        """Reads a file with car models and returns a list with no line breaks."""

        with open("car_models.txt", "r") as models:
            model_list = models.readlines()
            for i, model in enumerate(model_list):
                model_list[i] = model.strip()
            return model_list

    def makes_models(self):
        makes = self.read_makes()
        models = self.read_models()

        makes_models = dict()
        for make in makes:
            makes_models[make] = []


        for model in models:
            for make in makes_models.keys():
                if make.startswith(model[0]):
                    makes_models[make].append(model[2:])

        return makes_models


cars = CarsList()

cars.makes_models()