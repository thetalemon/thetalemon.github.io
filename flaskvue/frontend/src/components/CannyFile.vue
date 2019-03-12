<template>
  <div>
    <h2>↓画像↓</h2>
    <div v-if="uploadImage">
        <img :src="uploadImage">
    </div>
      <h2>↓結果↓</h2>
    <div v-if="processedImage">
        <img :src="processedImage">
    </div>
    <input type="file" @change="onFileChange">
    <p> red   : {{ ave_red }}</p>
    <p> green : {{ ave_green }}</p>
    <p> blue  : {{ ave_blue }}</p>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  data () {
    return {
      uploadImage: '',
      processedImage: ''
    }
  },
  methods: {
    onFileChange (e) {
      e.preventDefault()
      var file = e.target.files[0]
      if (file && file.type.match(/^image\/(png|jpeg)$/)) {
        this.uploadImage = URL.createObjectURL(file)
      }
      const reader = new FileReader()
      reader.onload = (e) => {
        this.postFile(e.target.result)
        console.log(e.target.result)
      }
      reader.readAsDataURL(file)
    },
    postFile (fileData) {
      const path = `http://localhost:5000/api/cannyFile`
      let formData = new FormData()
      formData.append('image', fileData)
      axios.post(path, formData)
        .then(response => {
          this.processedImage = response.data.result
          this.ave_red = response.data.red
          this.ave_green = response.data.green
          this.ave_blue = response.data.blue
          console.log(response.data.result)
        })
        .catch(error => {
          console.log(error)
        })
    }
  }
}
</script>
